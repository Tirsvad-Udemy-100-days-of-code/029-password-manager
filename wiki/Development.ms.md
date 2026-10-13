[English](Development) | [Dansk](Development.da) | **Bahasa Malaysia**

# Pembangunan

## Susun atur projek

- `src/mypass/`: aplikasi
- `tests/`: ujian pytest
- `docs/`: dokumen projek, ADR dan tangkapan skrin
- `wiki/`: sumber wiki ini

## Jalankan ujian

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## Integrasi berterusan

Aliran kerja `.gitea/workflows/ci.yml` memasang projek, menyemak pemformatan, lint, jenis dan YAML, dan menjalankan pytest pada setiap push dan pull request.

## Dokumentasi kod sumber

Bina dokumentasi HTML dengan Doxygen; kemudian buka `docs/doxygen/html/index.html`.

```bash
doxygen Doxyfile
```

## Penerbitan wiki

Halaman dalam `wiki/` diterbitkan ke wiki ini secara automatik apabila perubahan sampai ke `main` (aliran kerja `.gitea/workflows/publish-wiki.yml`). Sunting fail dalam `wiki/`, bukan halaman wiki dalam antara muka web: halaman yang tiada dalam `wiki/` akan dipadam.

## Keputusan reka bentuk

Papan keratan menggunakan kaedah Tkinter sendiri dan bukan `pyperclip`, jadi tiada apa yang perlu dipasang (ADR-0001 dalam `docs/adr/`).
