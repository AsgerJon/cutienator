//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/qtextedit.h>

//  QTextEdit::ExtraSelection::~ExtraSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14ExtraSelectionD1Ev(
    QTextEdit::ExtraSelection *self) {
  delete self;
}

#endif  // QT_CONFIG(textedit)
