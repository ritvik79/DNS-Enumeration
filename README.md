# DNS-Enumeration
DNS zone transfer (AXFR) using Python script

## Overview 
This python script attempts a DNS Zone Transfer (AXFR) to retrieve subdomains for a target domain by querying its nameservers. Zone transfers are typically used to synchronize DNS records between servers, but misconfigured DNS servers may expose sensitive information, making this a common reconnaissance technique in security assessments. **your own domains or those you have permission to audit**.  

# DNS Zone Transfer Script  

## ⚠️ Disclaimer  
This script is intended **for educational and security research purposes only**. **Unauthorized use against third-party domains is illegal** and may violate cybersecurity laws (such as the **Computer Fraud and Abuse Act (CFAA)** and other regulations).  

- **DO NOT use this tool on domains you do not own or have explicit permission to test.**  
- The author **is not responsible** for any misuse of this tool.  
- Ensure you have **proper authorization** before conducting security assessments.  

By using this script, you agree to use it **ethically and legally**.  

## 🛠️ Requirements  
This script requires **Python 3** and the `dnspython` library.  

