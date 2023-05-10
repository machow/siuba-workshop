-- this pandoc lua filter finds divs with an attribute
-- called data-tags="["solution-code"]
function Div(el)
  -- print(quarto.utils.dump(el))

  local tags = el.attributes["tags"]

  -- find if tags contains "solution-code"
  if tags and string.find(tags, "solution%-code") then
    local kwargs = {content = el.content, collapse = true, type = "tip", title = "Show solution"}
    return quarto.Callout(kwargs)
  end

  return el
end
