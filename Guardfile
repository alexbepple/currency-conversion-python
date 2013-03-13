notification :off

guard 'shell' do
  watch(/^test.*.py$/) {|m| `nosetests test/unit` }
end
