//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qaccessiblewidgets_p.h"
#include "qabstracttextdocumentlayout.h"
#include "qapplication.h"
#include "qclipboard.h"
#include "qtextdocument.h"
#include "qtextobject.h"
#if QT_CONFIG(textedit)
#include "qplaintextedit.h"
#include "qtextedit.h"
#include "private/qtextedit_p.h"
#endif
#include "qtextboundaryfinder.h"
#if QT_CONFIG(scrollbar)
#include "qscrollbar.h"
#endif
#include "qdebug.h"
#include <QApplication>
#if QT_CONFIG(stackedwidget)
#include <QStackedWidget>
#endif
#if QT_CONFIG(toolbox)
#include <QToolBox>
#endif
#if QT_CONFIG(mdiarea)
#include <QMdiArea>
#include <QMdiSubWindow>
#endif
#if QT_CONFIG(dialogbuttonbox)
#include <QDialogButtonBox>
#endif
#include <limits.h>
#if QT_CONFIG(rubberband)
#include <QRubberBand>
#endif
#if QT_CONFIG(textbrowser)
#include <QTextBrowser>
#endif
#if QT_CONFIG(calendarwidget)
#include <QCalendarWidget>
#endif
#if QT_CONFIG(itemviews)
#include <QAbstractItemView>
#endif
#if QT_CONFIG(dockwidget)
#include <QDockWidget>
#include <private/qdockwidget_p.h>
#endif
#if QT_CONFIG(mainwindow)
#include <QMainWindow>
#endif
#include <QFocusFrame>
#if QT_CONFIG(menu)
#include <QMenu>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 411, as _ZN23QAccessibleMdiSubWindow7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline void QAccessibleMdiSubWindow::setText(QAccessible::Text textType, const QString &text)
{
    if (textType == QAccessible::Name)
        mdiSubWindow()->setWindowTitle(text);
    else
        QAccessibleWidgetV2::setText(textType, text);
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 419, as _ZNK23QAccessibleMdiSubWindow5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline QAccessible::State QAccessibleMdiSubWindow::state() const
{
    QAccessible::State state;
    state.focusable = true;
    if (!mdiSubWindow()->isMaximized()) {
        state.movable = true;
        state.sizeable = true;
    }
    if (mdiSubWindow()->isAncestorOf(QApplication::focusWidget())
            || QApplication::focusWidget() == mdiSubWindow())
        state.focused = true;
    if (!mdiSubWindow()->isVisible())
        state.invisible = true;
    if (const QWidget *parent = mdiSubWindow()->parentWidget())
        if (!parent->contentsRect().contains(mdiSubWindow()->geometry()))
            state.offscreen = true;
    if (!mdiSubWindow()->isEnabled())
        state.disabled = true;
    return state;
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 440, as _ZNK23QAccessibleMdiSubWindow10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline int QAccessibleMdiSubWindow::childCount() const
{
    if (mdiSubWindow()->widget())
        return 1;
    return 0;
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 447, as _ZNK23QAccessibleMdiSubWindow5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline QAccessibleInterface *QAccessibleMdiSubWindow::child(int index) const
{
    QMdiSubWindow *source = mdiSubWindow();
    if (index != 0 || !source->widget())
        return nullptr;

    return QAccessible::queryAccessibleInterface(source->widget());
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 456, as _ZNK23QAccessibleMdiSubWindow12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline int QAccessibleMdiSubWindow::indexOfChild(const QAccessibleInterface *child) const
{
    if (child && child->object() && child->object() == mdiSubWindow()->widget())
        return 0;
    return -1;
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 463, as _ZNK23QAccessibleMdiSubWindow4rectEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline QRect QAccessibleMdiSubWindow::rect() const
{
    if (mdiSubWindow()->isHidden())
        return QRect();
    if (!mdiSubWindow()->parent())
        return QAccessibleWidgetV2::rect();
    const QPoint pos = mdiSubWindow()->mapToGlobal(QPoint(0, 0));
    return QRect(pos, mdiSubWindow()->size());
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 473, as _ZNK23QAccessibleMdiSubWindow12mdiSubWindowEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
inline QMdiSubWindow *QAccessibleMdiSubWindow::mdiSubWindow() const
{
    return static_cast<QMdiSubWindow *>(object());
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMdiSubWindow that Python can take functions over in. Every QAccessibleMdiSubWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef QString * (*CuteQAccessibleMdiSubWindowCall0)(const void *, int, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef void (*CuteQAccessibleMdiSubWindowCall1)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef const QAccessible::State * (*CuteQAccessibleMdiSubWindowCall2)(const void *, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef int (*CuteQAccessibleMdiSubWindowCall3)(const void *, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef void * (*CuteQAccessibleMdiSubWindowCall4)(const void *, int, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef int (*CuteQAccessibleMdiSubWindowCall5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
typedef const QRect * (*CuteQAccessibleMdiSubWindowCall6)(const void *, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleMdiSubWindowCall7)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleMdiSubWindowCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMdiSubWindowCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMdiSubWindowCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMdiSubWindowCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleMdiSubWindowCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMdiSubWindowCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMdiSubWindowCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMdiSubWindowCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMdiSubWindowCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMdiSubWindowCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMdiSubWindowCall18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMdiSubWindowCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMdiSubWindow : public QAccessibleMdiSubWindow {
public:
  using QAccessibleMdiSubWindow::QAccessibleMdiSubWindow;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  QString QAccessibleMdiSubWindow::text(QAccessible::Text textType)
  //      const
  QString text(QAccessible::Text textType) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall0 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(textType), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleMdiSubWindow::text(textType);
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  void QAccessibleMdiSubWindow::setText(QAccessible::Text textType,
  //      const QString &text)
  void setText(QAccessible::Text textType, const QString &text) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall1 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall1>(taken[1]);
      call(this, static_cast<int>(textType), &text, &handled);
      if (handled) return;
    }
    QAccessibleMdiSubWindow::setText(textType, text);
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  QAccessible::State QAccessibleMdiSubWindow::state() const
  QAccessible::State state() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall2 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall2>(taken[2]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleMdiSubWindow::state();
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  int QAccessibleMdiSubWindow::childCount() const
  int childCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall3 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMdiSubWindow::childCount();
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  QAccessibleInterface *QAccessibleMdiSubWindow::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall4 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall4>(taken[4]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMdiSubWindow::child(index);
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  int QAccessibleMdiSubWindow::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall5 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall5>(taken[5]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleMdiSubWindow::indexOfChild(child);
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
  //  QRect QAccessibleMdiSubWindow::rect() const
  QRect rect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall6 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleMdiSubWindow::rect();
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall7 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall8 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall9 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall10 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall11 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall12 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall13 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall14 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall15 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall15>(taken[15]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall16 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall17 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall17>(taken[17]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall18 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall18>(taken[18]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleMdiSubWindowCall19 call = reinterpret_cast<CuteQAccessibleMdiSubWindowCall19>(taken[19]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  void QAccessibleMdiSubWindow::setText(QAccessible::Text textType, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAccessibleMdiSubWindow7setTextEN11QAccessible4TextERK7QString(
    QAccessibleMdiSubWindow *self,
    QAccessible::Text textType,
    const QString *text) {
  self->setText(textType, *text);
}

//  QAccessible::State QAccessibleMdiSubWindow::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK23QAccessibleMdiSubWindow5stateEv(
    const QAccessibleMdiSubWindow *self) {
  return new QAccessible::State(self->state());
}

//  int QAccessibleMdiSubWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QAccessibleMdiSubWindow10childCountEv(
    const QAccessibleMdiSubWindow *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleMdiSubWindow::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK23QAccessibleMdiSubWindow5childEi(
    const QAccessibleMdiSubWindow *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleMdiSubWindow::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QAccessibleMdiSubWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMdiSubWindow *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QRect QAccessibleMdiSubWindow::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK23QAccessibleMdiSubWindow4rectEv(
    const QAccessibleMdiSubWindow *self) {
  return new QRect(self->rect());
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  QMdiSubWindow *QAccessibleMdiSubWindow::mdiSubWindow() const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZNK23QAccessibleMdiSubWindow12mdiSubWindowEv(
    const QAccessibleMdiSubWindow *self) {
  return self->mdiSubWindow();
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleMdiSubWindow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMdiSubWindow(
    QAccessibleMdiSubWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMdiSubWindow *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  void QAccessibleMdiSubWindow::setText(QAccessible::Text textType, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAccessibleMdiSubWindow7setTextEN11QAccessible4TextERK7QString(
    QAccessibleMdiSubWindow *self,
    QAccessible::Text textType,
    const QString *text) {
  self->QAccessibleMdiSubWindow::setText(textType, *text);
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  QAccessible::State QAccessibleMdiSubWindow::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK23QAccessibleMdiSubWindow5stateEv(
    const QAccessibleMdiSubWindow *self) {
  return new QAccessible::State(self->QAccessibleMdiSubWindow::state());
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  int QAccessibleMdiSubWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QAccessibleMdiSubWindow10childCountEv(
    const QAccessibleMdiSubWindow *self) {
  return self->QAccessibleMdiSubWindow::childCount();
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  QAccessibleInterface *QAccessibleMdiSubWindow::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK23QAccessibleMdiSubWindow5childEi(
    const QAccessibleMdiSubWindow *self,
    int index) {
  return self->QAccessibleMdiSubWindow::child(index);
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  int QAccessibleMdiSubWindow::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QAccessibleMdiSubWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMdiSubWindow *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleMdiSubWindow::indexOfChild(child);
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(mdiarea)
//  QRect QAccessibleMdiSubWindow::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK23QAccessibleMdiSubWindow4rectEv(
    const QAccessibleMdiSubWindow *self) {
  return new QRect(self->QAccessibleMdiSubWindow::rect());
}
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(accessibility)
