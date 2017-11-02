# CIDR Calculator

Tugas Kecil Jaringan Komputer IF3130

Created by Aldrich Valentino Halim - 13515081

### Prerequisites

Project is run by:
* [Makefile](https://www.gnu.org/software/make/)
* [Python 2.7](https://www.python.org/download/releases/2.7/)

## How To Run

```
make run
```

## Process each phase
### Phase 1 (fungsi getValidSubnet)
Subnet yang dikembalikan adalah host ditambah dengan `'/32'`. Hal ini menandakan bahwa jumlah host yang diperbolehkan oleh subnet tersebut adalah 2^32.

### Phase 2 (fungsi countHost)
Fungsi countHost akan mengambil angka di belakang tanda `/`. Jumlah host yang dikembalikan adalah 2 pangkat angka tersebut. Pangkat dihitung dengan menggunakan fungsi `<<` sebanyak angka subnet

### Phase 3 (fungsi isValidSubnet)
Pertama, host dan subnet akan diubah menjadi binary dengan menggunakan kombinasi fungsi `split()` dan `bin()`. Setelah itu, akan dibuat subnet mask dalam binary yang didapatkan dari angka subnet, yaitu setelah tanda `/`. Host dan Subnet akan di `AND` dengan subnet mask. Kedua hasil operasi ini akan dibandingkan, jika sama, maka hasilnya adalah `TRUE`, selain itu `FALSE`.

---

## Authors
**Aldrich Valentino** - [Aldrich Valentino](https://github.com/aldrichvalentino)
