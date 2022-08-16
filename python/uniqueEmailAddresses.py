class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ret = set()
        
        for i in range(len(emails)):
            local, domain = emails[i].split("@")
            
            local = local.replace(".","").split("+")[0]
                
            ret.add(local + "@" + domain)

        return len(ret)
            

        