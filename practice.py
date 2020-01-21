class TestAboveFreezing(nittest.TestCase):
   """ Tests for temperature.above_freezing."""
    
      def test_above_freezing_above(self):
          """Test a temperature that is above freezing."""
          
          expected = True 
          actual = temperature.above_freezing(5.2)
          self.assertEqual(expected, actual, "The temperature is above freezing.")
          
          
      def test_above_freezing_below(self):
          """Test a temperature that is below freezing."""
          
          expected = False
          actual = temperature.above_freezing(-2)
          self.assertEqual(expected, actual, 
             "The temperature is below freezing")
