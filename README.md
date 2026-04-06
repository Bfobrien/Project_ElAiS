—PROJECT ElAiS HOMELAB—


PURPOSE: Project ElAiS is an attempt at creating a home network that has various services, and hardware controlled by a local LLM. 

DEVICES: 
	- Raspberry Pi 5 (ElAiS): Hosts a local version of Llama 3.2:3B using Ollama with a modified model file. Accepts prompts from PiLOT and responds either conversationally, or with JSON data including the method requested and relevant parameters.

	- Raspberry Pi 4 (PiLOT): Prompts, and receives responses from ElAiS. 

	- Dell OptiPlex 3040: Windows Server

	- Lenovo ThinkPad W530: Wazuh (SIEM)

	- Cisco ASA 5510

	- Cisco 2800 Series Router

	- Cisco 3750G Switch

FILES:
	- ProjectElais_Homelab.pkt: PacketTracer file that mirrors the homelab as accurately as possible. Created to test configurations, and for demonstration purposes.

	- Houston.py: Python script running on PiLOT responsible for communication between PiLOT and ElAiS. 
	

