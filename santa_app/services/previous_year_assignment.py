import csv



class PreviousYearAssignmentReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_previous_pairs(self):
        """
        Returns a dictionary of {giver_email: receiver_email} from previous CSV
        """
        previous_pairs = {}
        try:
            with open(self.file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    previous_pairs[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        except FileNotFoundError:
            # No previous file, return empty dict
            previous_pairs = {}
        return previous_pairs
