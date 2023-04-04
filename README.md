# LUNA-Cipher

This is the LUNA Cipher. LUNA is an acryonym for Layered Unbreakable Numerical Algorithm. LUNA is an acronym named after my cat. This cipher will be based upon a previous cipher I created named the TESS Cipher. The TESS Cipher (Transformational Enhanced Shift System) used a modified version of the Ceaser Cipher which increases the shift used as it encrypts the message. The LUNA Cipher is based on the same principle, however, at the very end of the encryption, the whole message is put through the Polybius Cipher.

There is an additional version called LUNAF (Layered Unbreakable Numerical Algorithm for Files). This version of LUNA intakes a file and a shift value, and outputs an encrypted file.

NOTES:
 - The verbose output for decryption is not working for LUNA
 - The shift value is stored in the encrypted message for LUNA (not LUNAF)
   - To this extent, I would like to add an option to embed the shift or not
 - The code for LUNA is kinda garbage right now, I would like to recode it
