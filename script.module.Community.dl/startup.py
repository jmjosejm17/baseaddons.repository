

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyAgICAgIENvcHlyaWdodCAoQykgMjAxNSBTdXJmYWNpbmd4ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkgICAgICAgICMKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiwgb3IgKGF0IHlvdXIgb3B0aW9uKSAgICAgICAgICMKIyAgYW55IGxhdGVyIHZlcnNpb24uICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGRpc3RyaWJ1dGVkIGluIHRoZSBob3BlIHRoYXQgaXQgd2lsbCBiZSB1c2VmdWwsICAgICAgICAgICAgICMKIyAgYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YgICAgICAgICAgICAgICMKIyAgTUVSQ0hBTlRBQklMSVRZIG9yIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFLiBTZWUgdGhlICAgICAgICAgICAgICAgICMKIyAgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgZm9yIG1vcmUgZGV0YWlscy4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgWW91IHNob3VsZCBoYXZlIHJlY2VpdmVkIGEgY29weSBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgICAgICAgICAgICMKIyAgYWxvbmcgd2l0aCBYQk1DOyBzZWUgdGhlIGZpbGUgQ09QWUlORy4gIElmIG5vdCwgd3JpdGUgdG8gICAgICAgICAgICAgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbiwgNjc1IE1hc3MgQXZlLCBDYW1icmlkZ2UsIE1BIDAyMTM5LCBVU0EuICAgICAgICMKIyAgaHR0cDovL3d3dy5nbnUub3JnL2NvcHlsZWZ0L2dwbC5odG1sICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCmltcG9ydCB4Ym1jLCB4Ym1jYWRkb24sIHhibWNndWksIHhibWNwbHVnaW4sIG9zLCBzeXMsIHhibWN2ZnMsIGdsb2IKaW1wb3J0IHNodXRpbAppbXBvcnQgdXJsbGliMix1cmxsaWIKaW1wb3J0IHJlCmltcG9ydCB1c2VydmFyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGUsIGRhdGV0aW1lLCB0aW1lZGVsdGEKZnJvbSByZXNvdXJjZXMubGlicyBpbXBvcnQgZXh0cmFjdCwgZG93bmxvYWRlciwgbm90aWZ5LCBsb2dpbml0LCBkZWJyaWRpdCwgdHJha3RpdCwgc2tpblN3aXRjaCwgdXBsb2FkTG9nLCB3aXphcmQgYXMgd2l6CgpBRERPTl9JRCAgICAgICA9IHVzZXJ2YXIuQURET05fSUQKQURET05USVRMRSAgICAgPSB1c2VydmFyLkFERE9OVElUTEUKQURET04gICAgICAgICAgPSB3aXouYWRkb25JZChBRERPTl9JRCkKVkVSU0lPTiAgICAgICAgPSB3aXouYWRkb25JbmZvKEFERE9OX0lELCd2ZXJzaW9uJykKQURET05QQVRIICAgICAgPSB3aXouYWRkb25JbmZvKEFERE9OX0lELCdwYXRoJykKQURET05JRCAgICAgICAgPSB3aXouYWRkb25JbmZvKEFERE9OX0lELCdpZCcpCkRJQUxPRyAgICAgICAgID0geGJtY2d1aS5EaWFsb2coKQpEUCAgICAgICAgICAgICA9IHhibWNndWkuRGlhbG9nUHJvZ3Jlc3MoKQpIT01FICAgICAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aCgnc3BlY2lhbDovL2hvbWUvJykKUFJPRklMRSAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoJ3NwZWNpYWw6Ly9wcm9maWxlLycpCktPRElIT01FICAgICAgID0geGJtYy50cmFuc2xhdGVQYXRoKCdzcGVjaWFsOi8veGJtYy8nKQpBRERPTlMgICAgICAgICA9IG9zLnBhdGguam9pbihIT01FLCAgICAgJ2FkZG9ucycpCktPRElBRERPTlMgICAgID0gb3MucGF0aC5qb2luKEtPRElIT01FLCAnYWRkb25zJykKVVNFUkRBVEEgICAgICAgPSBvcy5wYXRoLmpvaW4oSE9NRSwgICAgICd1c2VyZGF0YScpClBMVUdJTiAgICAgICAgID0gb3MucGF0aC5qb2luKEFERE9OUywgICBBRERPTl9JRCkKUEFDS0FHRVMgICAgICAgPSBvcy5wYXRoLmpvaW4oQURET05TLCAgICdwYWNrYWdlcycpCkFERE9OREFUQSAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAnYWRkb25fZGF0YScsIEFERE9OX0lEKQpGQU5BUlQgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlBBVEgsJ2ZhbmFydC5qcGcnKQpJQ09OICAgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlBBVEgsJ2ljb24ucG5nJykKQVJUICAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oQURET05QQVRILCdyZXNvdXJjZXMnLCAnYXJ0JykKU0tJTiAgICAgICAgICAgPSB4Ym1jLmdldFNraW5EaXIoKQpCVUlMRE5BTUUgICAgICA9IHdpei5nZXRTKCdidWlsZG5hbWUnKQpERUZBVUxUU0tJTiAgICA9IHdpei5nZXRTKCdkZWZhdWx0c2tpbicpCkRFRkFVTFROQU1FICAgID0gd2l6LmdldFMoJ2RlZmF1bHRza2lubmFtZScpCkRFRkFVTFRJR05PUkUgID0gd2l6LmdldFMoJ2RlZmF1bHRza2luaWdub3JlJykKQlVJTERWRVJTSU9OICAgPSB3aXouZ2V0UygnYnVpbGR2ZXJzaW9uJykKQlVJTERMQVRFU1QgICAgPSB3aXouZ2V0UygnbGF0ZXN0dmVyc2lvbicpCkJVSUxEQ0hFQ0sgICAgID0gd2l6LmdldFMoJ2xhc3RidWlsZGNoZWNrJykKRElTQUJMRVVQREFURSAgPSB3aXouZ2V0UygnZGlzYWJsZXVwZGF0ZScpCkFVVE9DTEVBTlVQICAgID0gd2l6LmdldFMoJ2F1dG9jbGVhbicpCkFVVE9DQUNIRSAgICAgID0gd2l6LmdldFMoJ2NsZWFyY2FjaGUnKQpBVVRPUEFDS0FHRVMgICA9IHdpei5nZXRTKCdjbGVhcnBhY2thZ2VzJykKQVVUT1RIVU1CUyAgICAgPSB3aXouZ2V0UygnY2xlYXJ0aHVtYnMnKQpBVVRPRkVRICAgICAgICA9IHdpei5nZXRTKCdhdXRvY2xlYW5mZXEnKQpBVVRPTkVYVFJVTiAgICA9IHdpei5nZXRTKCduZXh0YXV0b2NsZWFudXAnKQpUUkFLVFNBVkUgICAgICA9IHdpei5nZXRTKCd0cmFrdGxhc3RzYXZlJykKUkVBTFNBVkUgICAgICAgPSB3aXouZ2V0UygnZGVicmlkbGFzdHNhdmUnKQpMT0dJTlNBVkUgICAgICA9IHdpei5nZXRTKCdsb2dpbmxhc3RzYXZlJykKS0VFUFRSQUtUICAgICAgPSB3aXouZ2V0Uygna2VlcHRyYWt0JykKS0VFUFJFQUwgICAgICAgPSB3aXouZ2V0Uygna2VlcGRlYnJpZCcpCktFRVBMT0dJTiAgICAgID0gd2l6LmdldFMoJ2tlZXBsb2dpbicpCklOU1RBTExFRCAgICAgID0gd2l6LmdldFMoJ2luc3RhbGxlZCcpCkVYVFJBQ1QgICAgICAgID0gd2l6LmdldFMoJ2V4dHJhY3QnKQpFWFRFUlJPUiAgICAgICA9IHdpei5nZXRTKCdlcnJvcnMnKQpOT1RJRlkgICAgICAgICA9IHdpei5nZXRTKCdub3RpZnknKQpOT1RFRElTTUlTUyAgICA9IHdpei5nZXRTKCdub3RlZGlzbWlzcycpCk5PVEVJRCAgICAgICAgID0gd2l6LmdldFMoJ25vdGVpZCcpCkJBQ0tVUExPQ0FUSU9OID0gQURET04uZ2V0U2V0dGluZygncGF0aCcpIGlmIG5vdCBBRERPTi5nZXRTZXR0aW5nKCdwYXRoJykgPT0gJycgZWxzZSBIT01FCk1ZQlVJTERTICAgICAgID0gb3MucGF0aC5qb2luKEJBQ0tVUExPQ0FUSU9OLCAnTXlfQnVpbGRzJywgJycpCk5PVEVJRCAgICAgICAgID0gMCBpZiBOT1RFSUQgPT0gIiIgZWxzZSBpbnQoTk9URUlEKQpBVVRPRkVRICAgICAgICA9IGludChBVVRPRkVRKSBpZiBBVVRPRkVRLmlzZGlnaXQoKSBlbHNlIDAKVE9EQVkgICAgICAgICAgPSBkYXRlLnRvZGF5KCkKVE9NT1JST1cgICAgICAgPSBUT0RBWSArIHRpbWVkZWx0YShkYXlzPTEpClRXT0RBWVMgICAgICAgID0gVE9EQVkgKyB0aW1lZGVsdGEoZGF5cz0yKQpUSFJFRURBWVMgICAgICA9IFRPREFZICsgdGltZWRlbHRhKGRheXM9MykKT05FV0VFSyAgICAgICAgPSBUT0RBWSArIHRpbWVkZWx0YShkYXlzPTcpCktPRElWICAgICAgICAgID0gZmxvYXQoeGJtYy5nZXRJbmZvTGFiZWwoIlN5c3RlbS5CdWlsZFZlcnNpb24iKVs6NF0pCkVYQ0xVREVTICAgICAgID0gdXNlcnZhci5FWENMVURFUwpCVUlMREZJTEUgICAgICA9IHVzZXJ2YXIuQlVJTERGSUxFClVQREFURUNIRUNLICAgID0gdXNlcnZhci5VUERBVEVDSEVDSyBpZiBzdHIodXNlcnZhci5VUERBVEVDSEVDSykuaXNkaWdpdCgpIGVsc2UgMQpORVhUQ0hFQ0sgICAgICA9IFRPREFZICsgdGltZWRlbHRhKGRheXM9VVBEQVRFQ0hFQ0spCk5PVElGSUNBVElPTiAgID0gdXNlcnZhci5OT1RJRklDQVRJT04KRU5BQkxFICAgICAgICAgPSB1c2VydmFyLkVOQUJMRQpIRUFERVJNRVNTQUdFICA9IHVzZXJ2YXIuSEVBREVSTUVTU0FHRQpBVVRPVVBEQVRFICAgICA9IHVzZXJ2YXIuQVVUT1VQREFURQpXSVpBUkRGSUxFICAgICA9IHVzZXJ2YXIuV0laQVJERklMRQpBVVRPSU5TVEFMTCAgICA9IHVzZXJ2YXIuQVVUT0lOU1RBTEwKUkVQT0lEICAgICAgICAgPSB1c2VydmFyLlJFUE9JRApSRVBPQURET05YTUwgICA9IHVzZXJ2YXIuUkVQT0FERE9OWE1MClJFUE9aSVBVUkwgICAgID0gdXNlcnZhci5SRVBPWklQVVJMCkNPTE9SMSAgICAgICAgID0gdXNlcnZhci5DT0xPUjEKQ09MT1IyICAgICAgICAgPSB1c2VydmFyLkNPTE9SMgpXT1JLSU5HICAgICAgICA9IFRydWUgaWYgd2l6LndvcmtpbmdVUkwoQlVJTERGSUxFKSA9PSBUcnVlIGVsc2UgRmFsc2UKRkFJTEVEICAgICAgICAgPSBGYWxzZQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMjIyMgQ2hlY2sgVXBkYXRlcyAgICMjIyMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKZGVmIGNoZWNrVXBkYXRlKCk6CglCVUlMRE5BTUUgICAgICA9IHdpei5nZXRTKCdidWlsZG5hbWUnKQoJQlVJTERWRVJTSU9OICAgPSB3aXouZ2V0UygnYnVpbGR2ZXJzaW9uJykKCWxpbmsgICAgICAgICAgID0gd2l6Lm9wZW5VUkwoQlVJTERGSUxFKS5yZXB'
love = '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'
god = 'dwYXRoKToKCQl3aXoubG9nKCJGb2xkZXIgYWxyZWFkeSBleGlzdHMsIGNsZWFuaW5nIEhvdXNlIiwgeGJtYy5MT0dOT1RJQ0UpCgkJd2l6LmNsZWFuSG91c2UobmV3cGF0aCkKCQl3aXoucmVtb3ZlRm9sZGVyKG5ld3BhdGgpCgl0cnk6CgkJd2l6LmNvcHl0cmVlKEFERE9OUEFUSCwgbmV3cGF0aCkKCWV4Y2VwdCBFeGNlcHRpb24sIGU6CgkJcGFzcwoJd2l6LmZvcmNlVXBkYXRlKFRydWUpCgp0cnk6CglteWJ1aWxkcyA9IHhibWMudHJhbnNsYXRlUGF0aChNWUJVSUxEUykKCWlmIG5vdCBvcy5wYXRoLmV4aXN0cyhteWJ1aWxkcyk6IHhibWN2ZnMubWtkaXJzKG15YnVpbGRzKQpleGNlcHQ6CglwYXNzCgp3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFN0YXJ0ZWQiLCB4Ym1jLkxPR05PVElDRSkKaWYgQVVUT0lOU1RBTEwgPT0gJ1llcycgYW5kIG5vdCBvcy5wYXRoLmV4aXN0cyhvcy5wYXRoLmpvaW4oQURET05TLCBSRVBPSUQpKToKCXdvcmtpbmd4bWwgPSB3aXoud29ya2luZ1VSTChSRVBPQURET05YTUwpCglpZiB3b3JraW5neG1sID09IFRydWU6CgkJdmVyID0gd2l6LnBhcnNlRE9NKHdpei5vcGVuVVJMKFJFUE9BRERPTlhNTCksICdhZGRvbicsIHJldD0ndmVyc2lvbicsIGF0dHJzID0geydpZCc6IFJFUE9JRH0pCgkJaWYgbGVuKHZlcikgPiAwOgoJCQlpbnN0YWxsemlwID0gJyVzLSVzLnppcCcgJSAoUkVQT0lELCB2ZXJbMF0pCgkJCXdvcmtpbmdyZXBvID0gd2l6LndvcmtpbmdVUkwoUkVQT1pJUFVSTCtpbnN0YWxsemlwKQoJCQlpZiB3b3JraW5ncmVwbyA9PSBUcnVlOgoJCQkJRFAuY3JlYXRlKEFERE9OVElUTEUsJ0Rvd25sb2FkaW5nIFJlcG8uLi4nLCcnLCAnUGxlYXNlIFdhaXQnKQoJCQkJaWYgbm90IG9zLnBhdGguZXhpc3RzKFBBQ0tBR0VTKTogb3MubWFrZWRpcnMoUEFDS0FHRVMpCgkJCQlsaWI9b3MucGF0aC5qb2luKFBBQ0tBR0VTLCBpbnN0YWxsemlwKQoJCQkJdHJ5OiBvcy5yZW1vdmUobGliKQoJCQkJZXhjZXB0OiBwYXNzCgkJCQlkb3dubG9hZGVyLmRvd25sb2FkKFJFUE9aSVBVUkwraW5zdGFsbHppcCxsaWIsIERQKQoJCQkJZXh0cmFjdC5hbGwobGliLCBBRERPTlMsIERQKQoJCQkJdHJ5OgoJCQkJCWYgPSBvcGVuKG9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCwgJ2FkZG9uLnhtbCcpLCBtb2RlPSdyJyk7IGcgPSBmLnJlYWQoKTsgZi5jbG9zZSgpCgkJCQkJbmFtZSA9IHdpei5wYXJzZURPTShnLCAnYWRkb24nLCByZXQ9J25hbWUnLCBhdHRycyA9IHsnaWQnOiBSRVBPSUR9KQoJCQkJCXdpei5Mb2dOb3RpZnkoIltDT0xPUiAlc10lc1svQ09MT1JdIiAlIChDT0xPUjEsIG5hbWVbMF0pLCAiW0NPTE9SICVzXUFkZC1vbiB1cGRhdGVkWy9DT0xPUl0iICUgQ09MT1IyLCBpY29uPW9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCwgJ2ljb24ucG5nJykpCgkJCQlleGNlcHQ6CgkJCQkJcGFzcwoJCQkJaWYgS09ESVYgPj0gMTc6IHdpei5hZGRvbkRhdGFiYXNlKFJFUE9JRCwgMSkKCQkJCURQLmNsb3NlKCkKCQkJCXhibWMuc2xlZXAoNTAwKQoJCQkJd2l6LmZvcmNlVXBkYXRlKFRydWUpCgkJCQl3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFN1Y2Nlc3NmdWxseSBJbnN0YWxsZWQiLCB4Ym1jLkxPR05PVElDRSkKCQkJZWxzZTogCgkJCQl3aXouTG9nTm90aWZ5KCJbQ09MT1IgJXNdUmVwbyBJbnN0YWxsIEVycm9yWy9DT0xPUl0iICUgQ09MT1IxLCAiW0NPTE9SICVzXUludmFsaWQgdXJsIGZvciB6aXAhWy9DT0xPUl0iICUgQ09MT1IyKQoJCQkJd2l6LmxvZygiW0F1dG8gSW5zdGFsbCBSZXBvXSBXYXMgdW5hYmxlIHRvIGNyZWF0ZSBhIHdvcmtpbmcgdXJsIGZvciByZXBvc2l0b3J5LiAlcyIgJSB3b3JraW5ncmVwbywgeGJtYy5MT0dFUlJPUikKCQllbHNlOgoJCQl3aXoubG9nKCJJbnZhbGlkIFVSTCBmb3IgUmVwbyBaaXAiLCB4Ym1jLkxPR0VSUk9SKQoJZWxzZTogCgkJd2l6LkxvZ05vdGlmeSgiW0NPTE9SICVzXVJlcG8gSW5zdGFsbCBFcnJvclsvQ09MT1JdIiAlIENPTE9SMSwgIltDT0xPUiAlc11JbnZhbGlkIGFkZG9uLnhtbCBmaWxlIVsvQ09MT1JdIiAlIENPTE9SMikKCQl3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFVuYWJsZSB0byByZWFkIHRoZSBhZGRvbi54bWwgZmlsZS4iLCB4Ym1jLkxPR0VSUk9SKQplbGlmIG5vdCBBVVRPSU5TVEFMTCA9PSAnWWVzJzogd2l6LmxvZygiW0F1dG8gSW5zdGFsbCBSZXBvXSBOb3QgRW5hYmxlZCIsIHhibWMuTE9HTk9USUNFKQplbGlmIG9zLnBhdGguZXhpc3RzKG9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCkpOiB3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFJlcG9zaXRvcnkgYWxyZWFkeSBpbnN0YWxsZWQiKQoKd2l6LmxvZygiW0F1dG8gVXBkYXRlIFdpemFyZF0gU3RhcnRlZCIsIHhibWMuTE9HTk9USUNFKQppZiBBVVRPVVBEQVRFID09ICdZZXMnOgoJd2l6LndpemFyZFVwZGF0ZSgnc3RhcnR1cCcpCmVsc2U6IHdpei5sb2coIltBdXRvIFVwZGF0ZSBXaXphcmRdIE5vdCBFbmFibGVkIiwgeGJtYy5MT0dOT1RJQ0UpCgp3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gU3RhcnRlZCIsIHhibWMuTE9HTk9USUNFKQppZiBFTkFCTEUgPT0gJ1llcyc6CglpZiBub3QgTk9USUZZID09ICd0cnVlJzoKCQl1cmwgPSB3aXoud29ya2luZ1VSTChOT1RJRklDQVRJT04pCgkJaWYgdXJsID09IFRydWU6CgkJCWlkLCBtc2cgPSB3aXouc3BsaXROb3RpZnkoTk9USUZJQ0FUSU9OKQoJCQlpZiBub3QgaWQgPT0gRmFsc2U6CgkJCQl0cnk6CgkJCQkJaWQgPSBpbnQoaWQpOyBOT1RFSUQgPSBpbnQoTk9URUlEKQoJCQkJCWlmIGlkID09IE5PVEVJRDoKCQkJCQkJaWYgTk9URURJU01JU1MgPT0gJ2ZhbHNlJzoKCQkJCQkJCW5vdGlmeS5ub3RpZmljYXRpb24obXNnKQoJCQkJCQllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gaWRbJXNdIERpc21pc3NlZCIgJSBpbnQoaWQpLCB4Ym1jLkxPR05PVElDRSkKCQkJCQllbGlmIGlkID4gTk9URUlEOgoJCQkJCQl3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gaWQ6ICVzIiAlIHN0cihpZCksIHhibWMuTE9HTk9USUNFKQoJCQkJCQl3aXouc2V0Uygnbm90ZWlkJywgc3RyKGlkKSkKCQkJCQkJd2l6LnNldFMoJ25vdGVkaXNtaXNzJywgJ2ZhbHNlJykKCQkJCQkJbm90aWZ5Lm5vdGlmaWNhdGlvbihtc2c9bXNnKQoJCQkJCQl3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gQ29tcGxldGUiLCB4Ym1jLkxPR05PVElDRSkKCQkJCWV4Y2VwdCBFeGNlcHRpb24sIGU6CgkJCQkJd2l6LmxvZygiRXJyb3Igb24gTm90aWZpY2F0aW9ucyBXaW5kb3c6ICVzIiAlIHN0cihlKSwgeGJtYy5MT0dFUlJPUikKCQkJZWxzZTogd2l6LmxvZygiW05vdGlmaWNhdGlvbnNdIFRleHQgRmlsZSBub3QgZm9ybWF0ZWQgQ29ycmVjdGx5IikKCQllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gVVJMKCVzKTogJXMiICUgKE5PVElGSUNBVElPTiwgdXJsKSwgeGJtYy5MT0dOT1RJQ0UpCgllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gVHVybmVkIE9mZiIsIHhibWMuTE9HTk9USUNFKQplbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gTm90IEVuYWJsZWQiLCB4Ym1jLkxPR05PVElDRSkKCndpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIFN0YXJ0ZWQiLCB4Ym1jLkxPR05PVElDRSkKaWYgSU5TVEFMTEVEID09ICd0cnVlJzoKCWlmIEtPRElWID49IDE3OgoJCXdpei5rb2RpMTdGaXgoKQoJCWlmIFNLSU4gaW4gWydza2luLmNvbmZsdWVuY2UnLCAnc2tpbi5lc3R1YXJ5J106CgkJCWNoZWNrU2tpbigpCgkJRkFJTEVEID0gVHJ1ZQoJZWxpZiBub3QgRVhUUkFDVCA9PSAnMTAwJyBhbmQgbm90IEJVSUxETkFNRSA9PSAiIjoKCQl3aXoubG9nKCJbSW5zdGFsbGVkIENoZWNrXSBCdWlsZCB3YXMgZXh0cmFjdGVkICVzLzEwMCB3aXRoIFtFUlJPUlM6ICVzXSIgJSAoRVhUUkFDVCwgRVhURVJST1IpLCB4Ym1jLkxPR05PVElDRSkKCQl5ZXM9RElBTE9HLnllc25vKEFERE9OVElUTEUsICdbQ09MT1IgJXNdJXNbL0NPTE9SXSBbQ09MT1IgJXNdd2FzIG5vdCBpbnN0YWxsZWQgY29ycmVjdGx5IScgJSAoQ09MT1IxLCBDT0xPUjIsIEJVSUxETkFNRSksICdJbnN0YWxsZWQ6IFtDT0xPUiAlc10lc1svQ09MT1JdIC8gRXJyb3IgQ291bnQ6IFtDT0xPUiAlc10lc1svQ09MT1JdJyAlIChDT0xPUjEsIEVYVFJBQ1QsIENPTE9SMSwgRVhURVJST1IpLCAnV291bGQgeW91IGxpa2UgdG8gdHJ5IGFnYWluP1svQ09MT1JdJywgbm9sYWJlbD0nW0JdTm8gVGhhbmtzIVsvQl0nLCB5ZXNsYWJlbD0nW0JdUmV0cnkgSW5zdGFsbFsvQl0nKQoJCXdpei5jbGVhclMoJ2J1aWxkJykKCQlGQUlMRUQgPSBUcnVlCgkJaWYgeWVzOiAKCQkJd2l6LmViaSgiUGxheU1lZGlhKHBsdWdpbjovLyVzLz9tb2RlPWluc3RhbGwmbmFtZT0lcyZ1cmw9ZnJlc2gpIiAlIChBRERPTl9JRCwgdXJsbGliLnF1b3RlX3BsdXMoQlVJTEROQU1FKSkpCgkJCXdpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIEZyZXNoIEluc3RhbGwgUmUtYWN0aXZhdGVkIiwgeGJtYy5MT0dOT1RJQ0UpCgkJZWxzZTogd2l6LmxvZygiW0luc3RhbGxlZCBDaGVja10gUmVpbnN0YWxsIElnbm9yZWQiKQoJZWxpZiBTS0lOIGluIFsnc2tpbi5jb25mbHVlbmNlJywgJ3NraW4uZXN0dWFyeSddOgoJCXdpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIEluY29ycmVjdCBza2luOiAlcyIgJSBTS0lOLCB4Ym1jLkxPR05PVElDRSkKCQlkZWZhdWx0cyA9IHdpei5nZXRTKCdkZWZhdWx0c2tpbicpCgkJaWYgbm90IGRlZmF1bHRzID09ICcnOgoJCQlpZiBvcy5wYXRoLmV4aXN0cyhvcy5wYXRoLmpvaW4oQURET05TLCBkZWZhdWx0cykpOgoJCQkJc2tpblN3aXRjaC5zd2FwU2tpbnMoZGVmYXVsdHMpCgkJCQl4ID0gMAoJCQkJeGJtYy5zbGVlcCgxMDAwKQoJCQkJd2hpbGUgbm90IHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoIldpbmRvdy5pc1Zpc2libGUoeWVzbm9kaWFsb2cpIikgYW5kIHggPCAxNTA6CgkJCQkJeCArPSAxCgkJCQkJeGJtYy5zbGVlcCgyMDApCgoJCQkJaWYgeGJtYy5nZXRDb25kVmlzaWJpbGl0eSgiV2luZG93LmlzVmlzaWJsZSh5ZXNub2RpYWxvZykiKToKCQkJCQl3aXouZWJpKCdTZW5kQ2xpY2soMTEpJykKCQkJCQl3aXoubG9va2FuZEZlZWxEYXRhKCdyZXN0b3JlJykKCQlpZiBub3Qgd2l6LmN1cnJTa2luKCkgPT0gZGVmYXVsdHMgYW5kIG5vdCBCVUlMRE5BTUUgPT0gIiI6CgkJCWd1aSA9IHdpei5jaGVja0J1aWxkKEJVSUxETkFNRSwgJ2d1aScpCgkJCUZBSUxFRCA9IFRydWUKCQkJaWYgZ3VpID09ICdodHRwOi8vJzoKCQkJCXdpei5sb2coIltJbnN0YWxsZWQgQ2hlY'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))