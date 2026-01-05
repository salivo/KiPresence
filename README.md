# KiPresence

**KiCad Discord Rich Presence** – a small system service that updates your Discord status with your KiCad activity.

---

## Installation

1. Clone this repo
2. Install with pacman:
```bash
cd KiPresence
makepkg -si
```
4. Enable the systemd service:
 ```bash
 sudo systemctl enable --now kipresence.service
 ```
## Usage

* The service will automatically start and update your Discord status.
* To check the service status:

  ```bash
  systemctl status kipresence.service
  ```

## License

MIT License – see `LICENSE` file.

---
