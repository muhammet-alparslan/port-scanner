    # Kullanıcıdan IP girişi isteniyor
    ip = input("Taramak istediğiniz IP adresini girin: ")

    # Kullanıcıdan port aralığı girişi isteniyor
    start_port = int(input("Tarama için başlangıç portunu girin: "))
    end_port = int(input("Tarama için bitiş portunu girin: "))

    # Kullanıcıdan tarama hızı seçimi isteniyor
    print("Tarama hızını seçin:")
    print("1. Hızlı")
    print("2. Orta")
    print("3. Yavaş")
    speed_choice = int(input("Seçiminizi girin (1-3): "))

    # Tarama hızını ayarlama
    if speed_choice == 1:
        timeout = 0.1
    elif speed_choice == 2:
        timeout = 0.5
    elif speed_choice == 3:
        timeout = 1
    else:
        print("Geçersiz seçim. Varsayılan olarak orta hız kullanılacak.")
        timeout = 0.5

    # Tarama fonksiyonu
    def port_taramasi(ip, start_port, end_port):
        try:
            open_ports = []  # Açık portları saklamak için bir liste

            for port in tqdm(range(start_port, end_port + 1), desc="Taranıyor"):
                # Soket oluşturma
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(timeout)

                # Portu tarama
                if s.connect_ex((ip, port)) == 0:
                    try:
                        service = socket.getservbyport(port)
                    except socket.error:
                        service = "Bilinmeyen servis"
                    open_ports.append((port, service))

                s.close()

            if open_ports:
                print("\nAçık portlar:")
                for port, service in open_ports:
                    print("Port {} ({}) açık".format(Fore.GREEN + str(port), service))
            else:
                print("\nAçık port bulunamadı.")

        except KeyboardInterrupt:
            print("\nTarama kullanıcı tarafından durduruldu.")
            exit()

        except socket.gaierror:
            print("Geçersiz bir host adı.")
            exit()

        except socket.error:
            print("Bağlantı hatası.")
            exit()

    # Taramayı başlatma
    port_taramasi(ip, start_port, end_port)