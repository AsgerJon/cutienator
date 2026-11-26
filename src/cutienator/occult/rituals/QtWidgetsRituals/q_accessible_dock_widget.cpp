//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qaccessiblewidgets_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextobject.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/qplaintextedit.h>
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/private/qtextedit_p.h>
#endif
#include <QtCore/qtextboundaryfinder.h>
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#include <QtCore/qdebug.h>
#include <QtWidgets/QApplication>
#if QT_CONFIG(stackedwidget)
#include <QtWidgets/QStackedWidget>
#endif
#if QT_CONFIG(toolbox)
#include <QtWidgets/QToolBox>
#endif
#if QT_CONFIG(mdiarea)
#include <QtWidgets/QMdiArea>
#include <QtWidgets/QMdiSubWindow>
#endif
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/QDialogButtonBox>
#endif
#include <limits.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/QRubberBand>
#endif
#if QT_CONFIG(textbrowser)
#include <QtWidgets/QTextBrowser>
#endif
#if QT_CONFIG(calendarwidget)
#include <QtWidgets/QCalendarWidget>
#endif
#if QT_CONFIG(itemviews)
#include <QtWidgets/QAbstractItemView>
#endif
#if QT_CONFIG(dockwidget)
#include <QtWidgets/QDockWidget>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(mainwindow)
#include <QtWidgets/QMainWindow>
#endif
#include <QtWidgets/QFocusFrame>
#if QT_CONFIG(menu)
#include <QtWidgets/QMenu>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 577, as _ZNK21QAccessibleDockWidget10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline int QAccessibleDockWidget::childCount() const
{
    if (dockWidget()->titleBarWidget()) {
        return dockWidget()->widget() ? 2 : 1;
    }
    return dockWidgetLayout()->count();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 600, as _ZNK21QAccessibleDockWidget12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline int QAccessibleDockWidget::indexOfChild(const QAccessibleInterface *child) const
{
    if (!child || !child->object() || child->object()->parent() != object())
        return -1;

    if (dockWidget()->titleBarWidget() == child->object()) {
        return dockWidget()->widget() ? 1 : 0;
    }

    return dockWidgetLayout()->indexOf(qobject_cast<QWidget*>(child->object()));
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 612, as _ZNK21QAccessibleDockWidget4rectEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline QRect QAccessibleDockWidget::rect() const
{
    QRect rect;

    if (dockWidget()->isFloating()) {
        rect = dockWidget()->frameGeometry();
    } else {
        rect = dockWidget()->rect();
        rect.moveTopLeft(dockWidget()->mapToGlobal(rect.topLeft()));
    }

    return rect;
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 641, as _ZNK21QAccessibleDockWidget4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline QAccessible::Role QAccessibleDockWidget::role() const
{
    if (dockWidget()->isFloating())
        return QAccessible::Window;

    return QAccessible::Pane;
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 585, as _ZNK21QAccessibleDockWidget5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline QAccessibleInterface *QAccessibleDockWidget::child(int index) const
{
    if (dockWidget()->titleBarWidget()) {
        if ((!dockWidget()->widget() && index == 0) || (index == 1))
            return QAccessible::queryAccessibleInterface(dockWidget()->titleBarWidget());
        if (index == 0)
            return QAccessible::queryAccessibleInterface(dockWidget()->widget());
    } else {
        QLayoutItem *item = dockWidgetLayout()->itemAt(index);
        if (item)
            return QAccessible::queryAccessibleInterface(item->widget());
    }
    return nullptr;
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 626, as _ZNK21QAccessibleDockWidget10dockWidgetEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline QDockWidget *QAccessibleDockWidget::dockWidget() const
{
    return static_cast<QDockWidget *>(object());
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 572, as _ZNK21QAccessibleDockWidget16dockWidgetLayoutEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
inline QDockWidgetLayout *QAccessibleDockWidget::dockWidgetLayout() const
{
    return qobject_cast<QDockWidgetLayout*>(dockWidget()->layout());
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleDockWidget that Python can take functions over in. Every QAccessibleDockWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef void * (*CuteQAccessibleDockWidgetCall0)(const void *, int, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef int (*CuteQAccessibleDockWidgetCall1)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef int (*CuteQAccessibleDockWidgetCall2)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef const QRect * (*CuteQAccessibleDockWidgetCall3)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef QString * (*CuteQAccessibleDockWidgetCall4)(const void *, int, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
typedef int (*CuteQAccessibleDockWidgetCall5)(const void *, int *);
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall6)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleDockWidgetCall7)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleDockWidgetCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleDockWidgetCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDockWidgetCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDockWidgetCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDockWidgetCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDockWidgetCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDockWidgetCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDockWidgetCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDockWidgetCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDockWidgetCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleDockWidget : public QAccessibleDockWidget {
public:
  using QAccessibleDockWidget::QAccessibleDockWidget;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[6] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
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
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  QAccessibleInterface *QAccessibleDockWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall0 call = reinterpret_cast<CuteQAccessibleDockWidgetCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleDockWidget::child(index);
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  int QAccessibleDockWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall1 call = reinterpret_cast<CuteQAccessibleDockWidgetCall1>(taken[1]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleDockWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  int QAccessibleDockWidget::childCount() const
  int childCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall2 call = reinterpret_cast<CuteQAccessibleDockWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleDockWidget::childCount();
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  QRect QAccessibleDockWidget::rect() const
  QRect rect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall3 call = reinterpret_cast<CuteQAccessibleDockWidgetCall3>(taken[3]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDockWidget::rect();
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  QString QAccessibleDockWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall4 call = reinterpret_cast<CuteQAccessibleDockWidgetCall4>(taken[4]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleDockWidget::text(t);
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
  //  QAccessible::Role QAccessibleDockWidget::role() const
  QAccessible::Role role() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall5 call = reinterpret_cast<CuteQAccessibleDockWidgetCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleDockWidget::role();
  }
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall6 call = reinterpret_cast<CuteQAccessibleDockWidgetCall6>(taken[6]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleWidgetV2::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall7 call = reinterpret_cast<CuteQAccessibleDockWidgetCall7>(taken[7]);
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
      CuteQAccessibleDockWidgetCall8 call = reinterpret_cast<CuteQAccessibleDockWidgetCall8>(taken[8]);
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
      CuteQAccessibleDockWidgetCall9 call = reinterpret_cast<CuteQAccessibleDockWidgetCall9>(taken[9]);
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
      CuteQAccessibleDockWidgetCall10 call = reinterpret_cast<CuteQAccessibleDockWidgetCall10>(taken[10]);
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
      CuteQAccessibleDockWidgetCall11 call = reinterpret_cast<CuteQAccessibleDockWidgetCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall12 call = reinterpret_cast<CuteQAccessibleDockWidgetCall12>(taken[12]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall13 call = reinterpret_cast<CuteQAccessibleDockWidgetCall13>(taken[13]);
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
      CuteQAccessibleDockWidgetCall14 call = reinterpret_cast<CuteQAccessibleDockWidgetCall14>(taken[14]);
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
      CuteQAccessibleDockWidgetCall15 call = reinterpret_cast<CuteQAccessibleDockWidgetCall15>(taken[15]);
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
      CuteQAccessibleDockWidgetCall16 call = reinterpret_cast<CuteQAccessibleDockWidgetCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall17 call = reinterpret_cast<CuteQAccessibleDockWidgetCall17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall18 call = reinterpret_cast<CuteQAccessibleDockWidgetCall18>(taken[18]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall19 call = reinterpret_cast<CuteQAccessibleDockWidgetCall19>(taken[19]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QAccessibleInterface::virtual_hook(id, data);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall20 call = reinterpret_cast<CuteQAccessibleDockWidgetCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleDockWidgetCall21 call = reinterpret_cast<CuteQAccessibleDockWidgetCall21>(taken[21]);
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

//  QAccessibleInterface *QAccessibleDockWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK21QAccessibleDockWidget5childEi(
    const QAccessibleDockWidget *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleDockWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleDockWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleDockWidget *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  int QAccessibleDockWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleDockWidget10childCountEv(
    const QAccessibleDockWidget *self) {
  return self->childCount();
}

//  QRect QAccessibleDockWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK21QAccessibleDockWidget4rectEv(
    const QAccessibleDockWidget *self) {
  return new QRect(self->rect());
}

//  QString QAccessibleDockWidget::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleDockWidget4textEN11QAccessible4TextE(
    const QAccessibleDockWidget *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleDockWidget::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK21QAccessibleDockWidget4roleEv(
    const QAccessibleDockWidget *self) {
  return self->role();
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  QDockWidget *QAccessibleDockWidget::dockWidget() const
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZNK21QAccessibleDockWidget10dockWidgetEv(
    const QAccessibleDockWidget *self) {
  return self->dockWidget();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  QDockWidgetLayout *QAccessibleDockWidget::dockWidgetLayout() const
extern "C" Q_DECL_EXPORT
QDockWidgetLayout *ritual_ZNK21QAccessibleDockWidget16dockWidgetLayoutEv(
    const QAccessibleDockWidget *self) {
  return self->dockWidgetLayout();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleDockWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleDockWidget(
    QAccessibleDockWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleDockWidget *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  QAccessibleInterface *QAccessibleDockWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK21QAccessibleDockWidget5childEi(
    const QAccessibleDockWidget *self,
    int index) {
  return self->QAccessibleDockWidget::child(index);
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  int QAccessibleDockWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleDockWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleDockWidget *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleDockWidget::indexOfChild(child);
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  int QAccessibleDockWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleDockWidget10childCountEv(
    const QAccessibleDockWidget *self) {
  return self->QAccessibleDockWidget::childCount();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  QRect QAccessibleDockWidget::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK21QAccessibleDockWidget4rectEv(
    const QAccessibleDockWidget *self) {
  return new QRect(self->QAccessibleDockWidget::rect());
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(dockwidget)
//  QAccessible::Role QAccessibleDockWidget::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK21QAccessibleDockWidget4roleEv(
    const QAccessibleDockWidget *self) {
  return self->QAccessibleDockWidget::role();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
