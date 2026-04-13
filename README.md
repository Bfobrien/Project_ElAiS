—PROJECT ElAiS HOMELAB—


PURPOSE: Project ElAiS is an attempt at creating a home network that has various services, and hardware controlled by a local LLM. 

DEVICES: 

	- Raspberry Pi 5 (Ai): Hosts a local version of Llama 3.2:3B using Ollama with a 
	modified model file. Accepts prompts from Ai Controller on RPi4, and responds either 
	conversationally, or with JSON data including the method requested and relevant parameters.

	- Raspberry Pi 4 (Ai Controller): Prompts, and receives responses from Ai on RPi5. 

	- Dell OptiPlex 3040: Windows Server
		- VM1: Hyper-V instance of TrueNAS, also acting as a Tailscale node

	- Lenovo ThinkPad W530: Wazuh (SIEM)

	- Cisco ASA 5510

	- Cisco 2800 Series Router

	- Cisco 3750G Switch

ADDITIONAL FILE EXPLANATIONS:

	- ProjectElais_Homelab.pkt: PacketTracer file that mirrors the homelab as accurately as 
possible. Created for demonstration purposes.

	- Houston.py: Python script running on RPi4 to send and receive communications to the Ai 
on RPi5. 

	- ElAiS_JSON_Test.png: Image showing that the Ai is capable of understanding the 
	difference between a command, and regular conversation, and respond appropriately to
	each. The Ai has been instructed in its modelfile that if it receives any commands, it will 
	not respond conversationally, but instead with JSON data including the method name, and that
	method's required parameters pulled from what the user requested. The modelfile will also 
	include a complete list of all methods, as well as their required parameters for the Ai's 
	reference. If information is missing, the Ai will request that information before passing the
	JSON formatted data back to the user.
	

