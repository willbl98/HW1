package pa6.view;

import pa6.model.Node;

/**
 * Purple-ish row header nodes
 */
class RowHeaderNodeView extends NodeView {
    RowHeaderNodeView(Node node) {
        super(node);
        _rectangle.getStyleClass().add("square-row-header");
    }
}
