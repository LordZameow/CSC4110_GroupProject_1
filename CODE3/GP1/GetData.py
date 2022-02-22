import SampleData
def main():
	"""
This transfers external data into

LOCAL data.

	"""

	print("Sample Data: " , dir(SampleData))

	localData = SampleData.SampleData

	print("\n\n")

	print("Local Data: " , localData)

if __name__ == "__main__":
	main()
print(main.__doc__)
input('END')
