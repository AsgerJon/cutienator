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
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 344, as _ZN18QAccessibleToolBoxC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbox)
inline QAccessibleToolBox::QAccessibleToolBox(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::LayeredPane)
{
    Q_ASSERT(qobject_cast<QToolBox *>(widget));
}
#endif  // QT_CONFIG(toolbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 350, as _ZNK18QAccessibleToolBox7toolBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbox)
inline QToolBox * QAccessibleToolBox::toolBox() const
{
    return static_cast<QToolBox *>(object());
}
#endif  // QT_CONFIG(toolbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleToolBox that Python can take functions over in. Every QAccessibleToolBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleToolBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleToolBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleToolBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleToolBoxCall5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleToolBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleToolBoxCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleToolBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleToolBoxCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleToolBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleToolBoxCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleToolBoxCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleToolBoxCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleToolBoxCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleToolBoxCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleToolBoxCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleToolBox : public QAccessibleToolBox {
public:
  using QAccessibleToolBox::QAccessibleToolBox;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
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
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall0 call = reinterpret_cast<CuteQAccessibleToolBoxCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall1 call = reinterpret_cast<CuteQAccessibleToolBoxCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall2 call = reinterpret_cast<CuteQAccessibleToolBoxCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall3 call = reinterpret_cast<CuteQAccessibleToolBoxCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall4 call = reinterpret_cast<CuteQAccessibleToolBoxCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall5 call = reinterpret_cast<CuteQAccessibleToolBoxCall5>(taken[5]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall6 call = reinterpret_cast<CuteQAccessibleToolBoxCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall7 call = reinterpret_cast<CuteQAccessibleToolBoxCall7>(taken[7]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall8 call = reinterpret_cast<CuteQAccessibleToolBoxCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall9 call = reinterpret_cast<CuteQAccessibleToolBoxCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall10 call = reinterpret_cast<CuteQAccessibleToolBoxCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall11 call = reinterpret_cast<CuteQAccessibleToolBoxCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleToolBoxCall12 call = reinterpret_cast<CuteQAccessibleToolBoxCall12>(taken[12]);
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
      CuteQAccessibleToolBoxCall13 call = reinterpret_cast<CuteQAccessibleToolBoxCall13>(taken[13]);
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
      CuteQAccessibleToolBoxCall14 call = reinterpret_cast<CuteQAccessibleToolBoxCall14>(taken[14]);
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
      CuteQAccessibleToolBoxCall15 call = reinterpret_cast<CuteQAccessibleToolBoxCall15>(taken[15]);
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
      CuteQAccessibleToolBoxCall16 call = reinterpret_cast<CuteQAccessibleToolBoxCall16>(taken[16]);
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
      CuteQAccessibleToolBoxCall17 call = reinterpret_cast<CuteQAccessibleToolBoxCall17>(taken[17]);
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
      CuteQAccessibleToolBoxCall18 call = reinterpret_cast<CuteQAccessibleToolBoxCall18>(taken[18]);
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
      CuteQAccessibleToolBoxCall19 call = reinterpret_cast<CuteQAccessibleToolBoxCall19>(taken[19]);
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
      CuteQAccessibleToolBoxCall20 call = reinterpret_cast<CuteQAccessibleToolBoxCall20>(taken[20]);
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
      CuteQAccessibleToolBoxCall21 call = reinterpret_cast<CuteQAccessibleToolBoxCall21>(taken[21]);
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

//  QAccessibleToolBox::QAccessibleToolBox(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAccessibleToolBox *ritual_ZN18QAccessibleToolBoxC1EP7QWidget(
    QWidget *widget) {
  return new CuteQAccessibleToolBox(widget);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbox)
//  QToolBox *QAccessibleToolBox::toolBox() const
extern "C" Q_DECL_EXPORT
QToolBox *ritual_ZNK18QAccessibleToolBox7toolBoxEv(
    const QAccessibleToolBox *self) {
  return self->toolBox();
}
#endif  // QT_CONFIG(toolbox)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleToolBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleToolBox(
    QAccessibleToolBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleToolBox *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
