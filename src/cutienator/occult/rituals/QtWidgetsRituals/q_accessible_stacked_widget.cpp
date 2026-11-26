//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 315, as _ZNK24QAccessibleStackedWidget10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline int QAccessibleStackedWidget::childCount() const
{
    return stackedWidget()->count();
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 320, as _ZNK24QAccessibleStackedWidget12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline int QAccessibleStackedWidget::indexOfChild(const QAccessibleInterface *child) const
{
    if (!child)
        return -1;

    QWidget *widget = qobject_cast<QWidget*>(child->object());
    return stackedWidget()->indexOf(widget);
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 329, as _ZNK24QAccessibleStackedWidget5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline QAccessibleInterface *QAccessibleStackedWidget::child(int index) const
{
    if (index < 0 || index >= stackedWidget()->count())
        return nullptr;
    return QAccessible::queryAccessibleInterface(stackedWidget()->widget(index));
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 302, as _ZNK24QAccessibleStackedWidget7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline QAccessibleInterface *QAccessibleStackedWidget::childAt(int x, int y) const
{
    if (!stackedWidget()->isVisible())
        return nullptr;
    QWidget *currentWidget = stackedWidget()->currentWidget();
    if (!currentWidget)
        return nullptr;
    QPoint position = currentWidget->mapFromGlobal(QPoint(x, y));
    if (currentWidget->rect().contains(position))
        return child(stackedWidget()->currentIndex());
    return nullptr;
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 296, as _ZN24QAccessibleStackedWidgetC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline QAccessibleStackedWidget::QAccessibleStackedWidget(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::LayeredPane)
{
    Q_ASSERT(qobject_cast<QStackedWidget *>(widget));
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 336, as _ZNK24QAccessibleStackedWidget13stackedWidgetEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
inline QStackedWidget *QAccessibleStackedWidget::stackedWidget() const
{
    return static_cast<QStackedWidget *>(object());
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleStackedWidget that Python can take functions over in. Every QAccessibleStackedWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleStackedWidgetCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleStackedWidgetCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall3)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall4)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleStackedWidgetCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleStackedWidgetCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleStackedWidgetCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleStackedWidgetCall11)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleStackedWidgetCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleStackedWidgetCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleStackedWidgetCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleStackedWidgetCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleStackedWidgetCall16)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleStackedWidgetCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleStackedWidgetCall18)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleStackedWidgetCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleStackedWidgetCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleStackedWidgetCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleStackedWidget : public QAccessibleStackedWidget {
public:
  using QAccessibleStackedWidget::QAccessibleStackedWidget;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
  //  QAccessibleInterface *QAccessibleStackedWidget::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall0 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall0>(taken[0]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleStackedWidget::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleStackedWidget::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall1 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleStackedWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleStackedWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall2 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall2>(taken[2]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleStackedWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleStackedWidget::child(int index)
  //      const
  QAccessibleInterface *child(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall3 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleStackedWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall4 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall5 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall6 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall7 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall8 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall9 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall9>(taken[9]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall10 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall11 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall11>(taken[11]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleWidget::text(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall12 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall13 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall13>(taken[13]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall14 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall15 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall16 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall16>(taken[16]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall17 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall18 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall18>(taken[18]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleStackedWidgetCall19 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall19>(taken[19]);
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
      CuteQAccessibleStackedWidgetCall20 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall20>(taken[20]);
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
      CuteQAccessibleStackedWidgetCall21 call = reinterpret_cast<CuteQAccessibleStackedWidgetCall21>(taken[21]);
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

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  QAccessibleStackedWidget::QAccessibleStackedWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAccessibleStackedWidget *ritual_ZN24QAccessibleStackedWidgetC1EP7QWidget(
    QWidget *widget) {
  return new CuteQAccessibleStackedWidget(widget);
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleInterface *QAccessibleStackedWidget::childAt(int x, int y)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK24QAccessibleStackedWidget7childAtEii(
    const QAccessibleStackedWidget *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  int QAccessibleStackedWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleStackedWidget10childCountEv(
    const QAccessibleStackedWidget *self) {
  return self->childCount();
}

//  int QAccessibleStackedWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAccessibleStackedWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleStackedWidget *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleStackedWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK24QAccessibleStackedWidget5childEi(
    const QAccessibleStackedWidget *self,
    int index) {
  return self->child(index);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  QStackedWidget *QAccessibleStackedWidget::stackedWidget() const
extern "C" Q_DECL_EXPORT
QStackedWidget *ritual_ZNK24QAccessibleStackedWidget13stackedWidgetEv(
    const QAccessibleStackedWidget *self) {
  return self->stackedWidget();
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleStackedWidget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleStackedWidget(
    QAccessibleStackedWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleStackedWidget *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  QAccessibleInterface *QAccessibleStackedWidget::childAt(int x, int y)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK24QAccessibleStackedWidget7childAtEii(
    const QAccessibleStackedWidget *self,
    int x,
    int y) {
  return self->QAccessibleStackedWidget::childAt(x, y);
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  int QAccessibleStackedWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QAccessibleStackedWidget10childCountEv(
    const QAccessibleStackedWidget *self) {
  return self->QAccessibleStackedWidget::childCount();
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  int QAccessibleStackedWidget::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QAccessibleStackedWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleStackedWidget *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleStackedWidget::indexOfChild(child);
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(stackedwidget)
//  QAccessibleInterface *QAccessibleStackedWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK24QAccessibleStackedWidget5childEi(
    const QAccessibleStackedWidget *self,
    int index) {
  return self->QAccessibleStackedWidget::child(index);
}
#endif  // QT_CONFIG(stackedwidget)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
