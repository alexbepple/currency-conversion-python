notification :off

guard 'shell' do
  watch(/^(src|test).*.py$/) {|m| `nosetests test/unit` }
end
