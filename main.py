import argparse
from dorkConverter import generatePhoneVariants, buildQueries


def main():
	parser = argparse.ArgumentParser(
		description="Generate search queries from a phone number"
	)

	parser.add_argument(
		"-p", "--phone",
		required=False,
		help="Phone number to generate dorks for"
	)

	args = parser.parse_args()

	if not args.phone:
		parser.error("You must provide at least --phone or -p")

	phone_number = args.phone

	variants = generatePhoneVariants(phone_number)
	queries = buildQueries(variants)

	for engine, query in queries.items():
		print(f"\n{engine.upper()} QUERY:\n{query}")


if __name__ == "__main__":
	main()