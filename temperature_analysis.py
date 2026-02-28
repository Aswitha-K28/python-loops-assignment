{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "611e46c6-7762-40f3-930c-ee76e57b2f61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Task 1:\n",
      "Celsius: [22 25 28 24 26]\n",
      "Fahrenheit: [71.6 77.  82.4 75.2 78.8]\n",
      "Average Fahrenheit: 77.0\n",
      "\n",
      "Task 2:\n",
      "Shape: (12,)\n",
      "Total elements: 12\n",
      "Highest score: 95\n",
      "Lowest score: 76\n",
      "Range: 19\n",
      "\n",
      "Task 3:\n",
      "NumPy sum: 1250025000\n",
      "Python sum: 1250025000\n",
      "NumPy time: 0.0002 seconds\n",
      "Python time: 0.0006 seconds\n",
      "NumPy is 2.9x faster\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import time\n",
    "\n",
    "# =========================\n",
    "# Task 1: Temperature Data Processing\n",
    "# =========================\n",
    "\n",
    "temps_celsius = np.array([22, 25, 28, 24, 26])\n",
    "temps_fahrenheit = temps_celsius * 1.8 + 32\n",
    "\n",
    "average_fahrenheit = round(np.mean(temps_fahrenheit), 1)\n",
    "\n",
    "print(\"Task 1:\")\n",
    "print(\"Celsius:\", temps_celsius)\n",
    "print(\"Fahrenheit:\", temps_fahrenheit)\n",
    "print(\"Average Fahrenheit:\", average_fahrenheit)\n",
    "print()\n",
    "\n",
    "\n",
    "# =========================\n",
    "# Task 2: Array Shape and Statistics\n",
    "# =========================\n",
    "\n",
    "scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])\n",
    "\n",
    "print(\"Task 2:\")\n",
    "print(\"Shape:\", scores.shape)\n",
    "print(\"Total elements:\", scores.size)\n",
    "print(\"Highest score:\", np.max(scores))\n",
    "print(\"Lowest score:\", np.min(scores))\n",
    "print(\"Range:\", np.max(scores) - np.min(scores))\n",
    "print()\n",
    "\n",
    "\n",
    "# =========================\n",
    "# Task 3: Performance Comparison\n",
    "# =========================\n",
    "\n",
    "numpy_array = np.arange(1, 50001)\n",
    "python_list = list(range(1, 50001))\n",
    "\n",
    "# NumPy timing\n",
    "start_numpy = time.time()\n",
    "numpy_sum = np.sum(numpy_array)\n",
    "end_numpy = time.time()\n",
    "numpy_time = end_numpy - start_numpy\n",
    "\n",
    "# Python timing\n",
    "start_python = time.time()\n",
    "python_sum = sum(python_list)\n",
    "end_python = time.time()\n",
    "python_time = end_python - start_python\n",
    "\n",
    "speed_factor = python_time / numpy_time\n",
    "\n",
    "print(\"Task 3:\")\n",
    "print(\"NumPy sum:\", numpy_sum)\n",
    "print(\"Python sum:\", python_sum)\n",
    "print(f\"NumPy time: {numpy_time:.4f} seconds\")\n",
    "print(f\"Python time: {python_time:.4f} seconds\")\n",
    "print(f\"NumPy is {speed_factor:.1f}x faster\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b29e09b-e23c-4692-8336-4b4ce7fdbd34",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
