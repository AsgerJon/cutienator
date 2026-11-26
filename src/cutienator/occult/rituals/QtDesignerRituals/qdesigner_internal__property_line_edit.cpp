//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/propertylineedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/propertylineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/propertylineedit_p.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qmenu.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/propertylineedit.cpp, line 20, as _ZN18qdesigner_internal16PropertyLineEdit5eventEP6QEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline bool PropertyLineEdit::event(QEvent *e)
    {
        // handle 'Select all' here as it is not done in the QLineEdit
        if (e->type() == QEvent::ShortcutOverride && !isReadOnly()) {
            QKeyEvent* ke = static_cast<QKeyEvent*> (e);
            if (ke->modifiers() & Qt::ControlModifier) {
                if(ke->key() == Qt::Key_A) {
                    ke->accept();
                    return true;
                }
            }
        }
        return QLineEdit::event(e);
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/propertylineedit.cpp, line 47, as _ZN18qdesigner_internal16PropertyLineEdit16contextMenuEventEP17QContextMenuEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void PropertyLineEdit::contextMenuEvent(QContextMenuEvent *event) {
        QMenu  *menu = createStandardContextMenu ();

        if (m_wantNewLine) {
            menu->addSeparator();
            menu->addAction(tr("Insert line break"), this, &PropertyLineEdit::insertNewLine);
        }

        menu->exec(event->globalPos());
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/propertylineedit.cpp, line 35, as _ZN18qdesigner_internal16PropertyLineEdit13insertNewLineEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void PropertyLineEdit::insertNewLine() {
        insertText(u"\\n"_s);
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/propertylineedit.cpp, line 39, as _ZN18qdesigner_internal16PropertyLineEdit10insertTextERK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void PropertyLineEdit::insertText(const QString &text) {
        // position cursor after new text and grab focus
        const int oldCursorPosition = cursorPosition ();
        insert(text);
        setCursorPosition (oldCursorPosition + text.size());
        setFocus(Qt::OtherFocusReason);
    }
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject *qdesigner_internal::PropertyLineEdit::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal16PropertyLineEdit10metaObjectEv(
    const qdesigner_internal::PropertyLineEdit *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::PropertyLineEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal16PropertyLineEdit11qt_metacastEPKc(
    qdesigner_internal::PropertyLineEdit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::PropertyLineEdit::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal16PropertyLineEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::PropertyLineEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void qdesigner_internal::PropertyLineEdit::setWantNewLine(bool nl)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16PropertyLineEdit14setWantNewLineEb(
    qdesigner_internal::PropertyLineEdit *self,
    bool nl) {
  self->setWantNewLine(nl);
}

//  bool qdesigner_internal::PropertyLineEdit::wantNewLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal16PropertyLineEdit11wantNewLineEv(
    const qdesigner_internal::PropertyLineEdit *self) {
  return self->wantNewLine();
}

//  bool qdesigner_internal::PropertyLineEdit::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal16PropertyLineEdit5eventEP6QEvent(
    qdesigner_internal::PropertyLineEdit *self,
    QEvent *e) {
  return self->event(e);
}

//  void
//      qdesigner_internal::PropertyLineEdit::contextMenuEvent(QContextMenuEv
//      ent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16PropertyLineEdit16contextMenuEventEP17QContextMenuEvent(
    qdesigner_internal::PropertyLineEdit *self,
    QContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void qdesigner_internal::PropertyLineEdit::insertNewLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16PropertyLineEdit13insertNewLineEv(
    qdesigner_internal::PropertyLineEdit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::PropertyLineEdit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "insertNewLine()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "insertNewLine()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::PropertyLineEdit::insertText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16PropertyLineEdit10insertTextERK7QString(
    qdesigner_internal::PropertyLineEdit *self,
    const QString *a0) {
  self->insertText(*a0);
}

//  bool qdesigner_internal::PropertyLineEdit::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal16PropertyLineEdit5eventEP6QEvent(
    qdesigner_internal::PropertyLineEdit *self,
    QEvent *e) {
  return self->qdesigner_internal::PropertyLineEdit::event(e);
}
