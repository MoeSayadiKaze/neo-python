from unittest import TestCase
import pexpect


class PromptTest(TestCase):

    def test_prompt_run(self):

        child = pexpect.spawn('python neo/bin/prompt.py')
        child.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=10)  # if test is failing consider increasing timeout time
        before = child.before
        text = before.decode('utf-8', 'ignore')
        checktext = "neo>"
        self.assertIn(checktext, text)
        child.terminate()

    def test_prompt_open_wallet(self):

        child = pexpect.spawn('python neo/bin/prompt.py')
        child.send('open wallet fixtures/testwallet.db3\n')
        child.send('testpassword\n')
        child.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=15)  # if test is failing consider increasing timeout time
        before = child.before
        text = before.decode('utf-8', 'ignore')
        checktext = "Opened"
        self.assertIn(checktext, text)
        child.terminate()
