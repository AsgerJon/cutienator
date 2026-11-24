//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "simplewidgets_p.h"
#if QT_CONFIG(abstractbutton)
#include <qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(label)
#include <qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#include <private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <qmessagebox.h>
#endif
#include <qstyle.h>
#include <qstyleoption.h>
#include <qtextdocument.h>
#include <qwindow.h>
#include <private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <qfocusframe.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/simplewidgets.cpp, line 962, as _ZN21QAccessibleMessageBoxC1EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
inline QAccessibleMessageBox::QAccessibleMessageBox(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::AlertMessage)
{
    Q_ASSERT(qobject_cast<QMessageBox *>(widget));
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 973, as _ZNK21QAccessibleMessageBox4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
inline QString QAccessibleMessageBox::text(QAccessible::Text t) const
{
    QString str;

    switch (t) {
    case QAccessible::Name:
        str = QAccessibleWidgetV2::text(t);
        if (str.isEmpty()) // implies no title text is set
            str = messageBox()->text();
        break;
    case QAccessible::Value:
        str = messageBox()->text();
        break;
    case QAccessible::Help:
        str = messageBox()->informativeText();
        break;
    default:
        str = QAccessibleWidgetV2::text(t);
        break;
    }

    return str;
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 968, as _ZNK21QAccessibleMessageBox10messageBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
inline QMessageBox *QAccessibleMessageBox::messageBox() const
{
    return static_cast<QMessageBox *>(widget());
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMessageBox that Python can take functions over in. Every QAccessibleMessageBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
typedef QString * (*CuteQAccessibleMessageBoxCall0)(const void *, int, int *);
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleMessageBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleMessageBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleMessageBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleMessageBoxCall5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleMessageBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleMessageBoxCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleMessageBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMessageBoxCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMessageBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMessageBoxCall14)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMessageBoxCall16)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMessageBoxCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMessageBoxCall18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMessageBoxCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMessageBox : public QAccessibleMessageBox {
public:
  using QAccessibleMessageBox::QAccessibleMessageBox;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
#if QT_CONFIG(messagebox)
  //  QString QAccessibleMessageBox::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall0 call = reinterpret_cast<CuteQAccessibleMessageBoxCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleMessageBox::text(t);
  }
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall1 call = reinterpret_cast<CuteQAccessibleMessageBoxCall1>(taken[1]);
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
      CuteQAccessibleMessageBoxCall2 call = reinterpret_cast<CuteQAccessibleMessageBoxCall2>(taken[2]);
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
      CuteQAccessibleMessageBoxCall3 call = reinterpret_cast<CuteQAccessibleMessageBoxCall3>(taken[3]);
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
      CuteQAccessibleMessageBoxCall4 call = reinterpret_cast<CuteQAccessibleMessageBoxCall4>(taken[4]);
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
      CuteQAccessibleMessageBoxCall5 call = reinterpret_cast<CuteQAccessibleMessageBoxCall5>(taken[5]);
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
      CuteQAccessibleMessageBoxCall6 call = reinterpret_cast<CuteQAccessibleMessageBoxCall6>(taken[6]);
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
      CuteQAccessibleMessageBoxCall7 call = reinterpret_cast<CuteQAccessibleMessageBoxCall7>(taken[7]);
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
      CuteQAccessibleMessageBoxCall8 call = reinterpret_cast<CuteQAccessibleMessageBoxCall8>(taken[8]);
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
      CuteQAccessibleMessageBoxCall9 call = reinterpret_cast<CuteQAccessibleMessageBoxCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall10 call = reinterpret_cast<CuteQAccessibleMessageBoxCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall11 call = reinterpret_cast<CuteQAccessibleMessageBoxCall11>(taken[11]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall12 call = reinterpret_cast<CuteQAccessibleMessageBoxCall12>(taken[12]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall13 call = reinterpret_cast<CuteQAccessibleMessageBoxCall13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall14 call = reinterpret_cast<CuteQAccessibleMessageBoxCall14>(taken[14]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall15 call = reinterpret_cast<CuteQAccessibleMessageBoxCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall16 call = reinterpret_cast<CuteQAccessibleMessageBoxCall16>(taken[16]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleMessageBoxCall17 call = reinterpret_cast<CuteQAccessibleMessageBoxCall17>(taken[17]);
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
      CuteQAccessibleMessageBoxCall18 call = reinterpret_cast<CuteQAccessibleMessageBoxCall18>(taken[18]);
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
      CuteQAccessibleMessageBoxCall19 call = reinterpret_cast<CuteQAccessibleMessageBoxCall19>(taken[19]);
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
#if QT_CONFIG(messagebox)
//  QAccessibleMessageBox::QAccessibleMessageBox(QWidget *widget)
extern "C" Q_DECL_EXPORT
QAccessibleMessageBox *ritual_ZN21QAccessibleMessageBoxC1EP7QWidget(
    QWidget *widget) {
  return new CuteQAccessibleMessageBox(widget);
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

//  QString QAccessibleMessageBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleMessageBox4textEN11QAccessible4TextE(
    const QAccessibleMessageBox *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
//  QMessageBox *QAccessibleMessageBox::messageBox() const
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZNK21QAccessibleMessageBox10messageBoxEv(
    const QAccessibleMessageBox *self) {
  return self->messageBox();
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleMessageBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMessageBox(
    QAccessibleMessageBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMessageBox *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(messagebox)
//  QString QAccessibleMessageBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QAccessibleMessageBox4textEN11QAccessible4TextE(
    const QAccessibleMessageBox *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleMessageBox::text(t));
}
#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(accessibility)
