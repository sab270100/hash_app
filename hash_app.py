import streamlit as st
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
st.write("""
# Fungsi Hash
""")

input = st.text_input('Masukkan Teks', 'Universitas Respati Yogyakarta')
digest.update(input.encode())
hash = digest.finalize()
st.write('Hash :', hash.hex())
