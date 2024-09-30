{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f87cb49-132d-4eb1-875e-4c92a0716152",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task №1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "352f4ed4-aaad-43da-a14f-b2f45f484d5c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st integer:  5\n",
      "Enter 2nd integer:  7\n",
      "Enter 3d integer:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5, 7, 9\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter 1st integer: \"))\n",
    "b = int(input(\"Enter 2nd integer: \"))\n",
    "c = int(input(\"Enter 3d integer: \"))\n",
    "if a > b:\n",
    "    temp = a\n",
    "    a = b\n",
    "    b = temp\n",
    "if b > c:\n",
    "    temp = b\n",
    "    b = c\n",
    "    c = temp\n",
    "if a > b:\n",
    "    temp = a\n",
    "    a = b\n",
    "    b = temp\n",
    "print(f\"{a}, {b}, {c}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33f2e3a8-1a7b-4621-84b5-d353d7b420ae",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
