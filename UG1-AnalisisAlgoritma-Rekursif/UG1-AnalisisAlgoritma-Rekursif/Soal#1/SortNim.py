def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.

    if current_length == 0:
        return [current_value]

    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        if sorted_array[current_length - 1] <= current_value:
            return sorted_array[:current_length] + [current_value]

    else:
        if sorted_array[current_length - 1] >= current_value:
            return sorted_array[:current_length] + [current_value]

    hasil = InsertRecursive(
        sorted_array[:current_length - 1],
        current_value,
        current_length - 1
    )

    return hasil + [sorted_array[current_length - 1]]


def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.

    if current_length == 0:
        return []

    hasil_sebelumnya = RecursiveFilterSort(
        data_array,
        current_length - 1
    )

    nilai_sekarang = data_array[current_length - 1]

    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        if nilai_sekarang % 2 != 0:
            return InsertRecursive(
                hasil_sebelumnya,
                nilai_sekarang,
                len(hasil_sebelumnya)
            )

    else:
        if nilai_sekarang % 2 == 0:
            return InsertRecursive(
                hasil_sebelumnya,
                nilai_sekarang,
                len(hasil_sebelumnya)
            )

    return hasil_sebelumnya


# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0]
NIM_MAHASISWA = "71251212"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 3: cetak hasil akhir sesuai format yang diminta.
    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        tipe = "GANJIL (Ascending)"
    else:
        tipe = "GENAP (Descending)"

    print("====== FILTER & SORT NIM ======")
    print("NIM Mahasiswa   :", NIM_MAHASISWA)
    print("Tipe            :", tipe)
    print("Data Digit Awal :", raw_data)
    print("Hasil Akhir     :", final_result)