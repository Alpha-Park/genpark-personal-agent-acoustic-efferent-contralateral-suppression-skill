"""
MCP Server for Acoustic Efferent Contralateral Suppression Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating MOC suppression magnitude (dB), OAE damping, and auditory gating.
"""

import sys
import json
from typing import Dict, Any
from client import AcousticEfferentSuppressionClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_contralateral_suppression",
                "description": "Calculates Medial Olivocochlear (MOC) Efferent Contralateral Suppression magnitude (dB), speech-in-noise gating, and auditory protective resilience score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_oae_amplitude_db_spl": {
                            "type": "number",
                            "description": "Baseline Otoacoustic Emission (DPOAE/TEOAE) amplitude in dB SPL (e.g. 10.5 dB SPL)."
                        },
                        "noise_conditioned_oae_amplitude_db_spl": {
                            "type": "number",
                            "description": "OAE amplitude during contralateral acoustic noise stimulation in dB SPL (e.g. 8.8 dB SPL)."
                        },
                        "contralateral_noise_db_spl": {
                            "type": "number",
                            "description": "Contralateral broadband noise level in dB SPL (normative 60-65 dB SPL, default: 65.0 dB SPL).",
                            "default": 65.0
                        },
                        "test_frequency_hz": {
                            "type": "integer",
                            "description": "Acoustic center test frequency in Hz (default: 2000 Hz).",
                            "default": 2000
                        }
                    },
                    "required": ["baseline_oae_amplitude_db_spl", "noise_conditioned_oae_amplitude_db_spl"]
                }
            }
        ]
    }


def handle_request(client: AcousticEfferentSuppressionClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_contralateral_suppression":
            res = client.evaluate_contralateral_suppression(
                baseline_oae_amplitude_db_spl=float(args.get("baseline_oae_amplitude_db_spl", 10.0)),
                noise_conditioned_oae_amplitude_db_spl=float(args.get("noise_conditioned_oae_amplitude_db_spl", 8.4)),
                contralateral_noise_db_spl=float(args.get("contralateral_noise_db_spl", 65.0)),
                test_frequency_hz=int(args.get("test_frequency_hz", 2000))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = AcousticEfferentSuppressionClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
