import hashlib


class JobAdd():
    add_url     = ""
    company_url = ""
    company     = ""
    add_heading = ""
    add_content = ""

    def get_hash(self):
        """
        Hashing function to create an unique job id
        """
        add_data = self.add_url+self.company_url+self.company + \
            self.add_heading+self.add_content
        return hashlib.md5(add_data.encode()).hexdigest()

    def get_dict(self):
        """
        Distill object into a dictionary and return it
        """
        return {
                "id"         : self.get_hash(),
                "add_url"    : self.add_url,
                "company_url": self.company_url,
                "company"    : self.company,
                "add_heading": self.add_heading,
                "add_content": self.add_content
                }
