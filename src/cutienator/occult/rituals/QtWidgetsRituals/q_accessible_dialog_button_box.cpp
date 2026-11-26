//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dialogbuttonbox)
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 481, as _ZN26QAccessibleDialogButtonBoxC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(dialogbuttonbox)
inline QAccessibleDialogButtonBox::QAccessibleDialogButtonBox(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::Grouping)
{
    Q_ASSERT(qobject_cast<QDialogButtonBox*>(widget));
}
#endif  // QT_CONFIG(dialogbuttonbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleDialogButtonBox that Python can take functions over in. Every QAccessibleDialogButtonBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleDialogButtonBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleDialogButtonBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDialogButtonBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDialogButtonBoxCall5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleDialogButtonBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDialogButtonBoxCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDialogButtonBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleDialogButtonBoxCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDialogButtonBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDialogButtonBoxCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDialogButtonBoxCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDialogButtonBoxCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDialogButtonBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDialogButtonBoxCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDialogButtonBoxCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDialogButtonBoxCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleDialogButtonBox : public QAccessibleDialogButtonBox {
public:
  using QAccessibleDialogButtonBox::QAccessibleDialogButtonBox;
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
      CuteQAccessibleDialogButtonBoxCall0 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall0>(taken[0]);
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
      CuteQAccessibleDialogButtonBoxCall1 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall1>(taken[1]);
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
      CuteQAccessibleDialogButtonBoxCall2 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall2>(taken[2]);
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
      CuteQAccessibleDialogButtonBoxCall3 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall3>(taken[3]);
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
      CuteQAccessibleDialogButtonBoxCall4 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall4>(taken[4]);
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
      CuteQAccessibleDialogButtonBoxCall5 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall5>(taken[5]);
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
      CuteQAccessibleDialogButtonBoxCall6 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall6>(taken[6]);
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
      CuteQAccessibleDialogButtonBoxCall7 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall7>(taken[7]);
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
      CuteQAccessibleDialogButtonBoxCall8 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall8>(taken[8]);
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
      CuteQAccessibleDialogButtonBoxCall9 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall9>(taken[9]);
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
      CuteQAccessibleDialogButtonBoxCall10 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall10>(taken[10]);
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
      CuteQAccessibleDialogButtonBoxCall11 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall11>(taken[11]);
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
      CuteQAccessibleDialogButtonBoxCall12 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall12>(taken[12]);
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
      CuteQAccessibleDialogButtonBoxCall13 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall13>(taken[13]);
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
      CuteQAccessibleDialogButtonBoxCall14 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall14>(taken[14]);
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
      CuteQAccessibleDialogButtonBoxCall15 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall15>(taken[15]);
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
      CuteQAccessibleDialogButtonBoxCall16 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall16>(taken[16]);
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
      CuteQAccessibleDialogButtonBoxCall17 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall17>(taken[17]);
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
      CuteQAccessibleDialogButtonBoxCall18 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall18>(taken[18]);
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
      CuteQAccessibleDialogButtonBoxCall19 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall19>(taken[19]);
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
      CuteQAccessibleDialogButtonBoxCall20 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall20>(taken[20]);
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
      CuteQAccessibleDialogButtonBoxCall21 call = reinterpret_cast<CuteQAccessibleDialogButtonBoxCall21>(taken[21]);
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

//  QAccessibleDialogButtonBox::QAccessibleDialogButtonBox(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAccessibleDialogButtonBox *ritual_ZN26QAccessibleDialogButtonBoxC1EP7QWidget(
    QWidget *widget) {
  return new CuteQAccessibleDialogButtonBox(widget);
}

//  a Python function taken by a CuteQAccessibleDialogButtonBox, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleDialogButtonBox(
    QAccessibleDialogButtonBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleDialogButtonBox *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dialogbuttonbox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
