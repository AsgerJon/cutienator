//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickWidgets/6.12.0/QtQuickWidgets/private/qaccessiblequickwidget_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickWidgets/qtquickwidgetsglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickWidgets/QtQuickWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickWidgets/6.12.0/QtQuickWidgets/private/qaccessiblequickwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickWidgets/private/qaccessiblequickwidget_p.h>
#include <QtQuickWidgets/private/qquickwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 68, as _ZNK37QAccessibleQuickWidgetOffscreenWindow5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleQuickWidgetOffscreenWindow::child(int index) const
{
    Q_UNUSED(index);
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 74, as _ZNK37QAccessibleQuickWidgetOffscreenWindow10childCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleQuickWidgetOffscreenWindow::childCount() const
{
    return 0;
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 79, as _ZNK37QAccessibleQuickWidgetOffscreenWindow12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const QAccessibleInterface *iface) const
{
    Q_UNUSED(iface);
    return -1;
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleQuickWidgetOffscreenWindow that Python can take functions over in. Every QAccessibleQuickWidgetOffscreenWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetOffscreenWindowCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetOffscreenWindowCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetOffscreenWindowCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleQuickWidgetOffscreenWindowCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickWidgetOffscreenWindowCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickWidgetOffscreenWindowCall9)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickWidgetOffscreenWindowCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetOffscreenWindowCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickWidgetOffscreenWindowCall13)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickWidgetOffscreenWindowCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickWidgetOffscreenWindowCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleQuickWidgetOffscreenWindow : public QAccessibleQuickWidgetOffscreenWindow {
public:
  using QAccessibleQuickWidgetOffscreenWindow::QAccessibleQuickWidgetOffscreenWindow;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface
  //      *QAccessibleQuickWidgetOffscreenWindow::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall0 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWidgetOffscreenWindow::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickWidgetOffscreenWindow::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall1 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickWidgetOffscreenWindow::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const
  //      QAccessibleInterface *iface) const
  int indexOfChild(const QAccessibleInterface *iface) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall2 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall2>(taken[2]);
      int given = call(this, iface, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickWidgetOffscreenWindow::indexOfChild(iface);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface
  //      *QAccessibleQuickWidgetOffscreenWindow::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall3 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall3>(taken[3]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWidgetOffscreenWindow::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickWindow::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall4 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWindow::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickWindow::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall5 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWindow::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleQuickWindow::role() const
  QAccessible::Role role() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall6 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleQuickWindow::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleQuickWindow::state() const
  QAccessible::State state() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall7 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall7>(taken[7]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickWindow::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleQuickWindow::rect() const
  QRect rect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall8 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall8>(taken[8]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickWindow::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleQuickWindow::text(QAccessible::Text text) const
  QString text(QAccessible::Text text) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall9 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall9>(taken[9]);
      QString * given = call(this, static_cast<int>(text), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleQuickWindow::text(text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QQuickWindow *QAccessibleQuickWindow::window() const
  QQuickWindow *window() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall10 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickWindow *>(given);
    }
    return QAccessibleQuickWindow::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleObject::isValid() const
  bool isValid() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall11 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleObject::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall12 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall13 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall13>(taken[13]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall14 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetOffscreenWindowCall15 call = reinterpret_cast<CuteQAccessibleQuickWidgetOffscreenWindowCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleInterface *QAccessibleQuickWidgetOffscreenWindow::child(int
//      index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow5childEi(
    const QAccessibleQuickWidgetOffscreenWindow *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleQuickWidgetOffscreenWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow10childCountEv(
    const QAccessibleQuickWidgetOffscreenWindow *self) {
  return self->childCount();
}

//  int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const
//      QAccessibleInterface *iface) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK37QAccessibleQuickWidgetOffscreenWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWidgetOffscreenWindow *self,
    const QAccessibleInterface *iface) {
  return self->indexOfChild(iface);
}

//  a Python function taken by a CuteQAccessibleQuickWidgetOffscreenWindow,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleQuickWidgetOffscreenWindow(
    QAccessibleQuickWidgetOffscreenWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleQuickWidgetOffscreenWindow *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleQuickWidgetOffscreenWindow::child(int
//      index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow5childEi(
    const QAccessibleQuickWidgetOffscreenWindow *self,
    int index) {
  return self->QAccessibleQuickWidgetOffscreenWindow::child(index);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleQuickWidgetOffscreenWindow::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow10childCountEv(
    const QAccessibleQuickWidgetOffscreenWindow *self) {
  return self->QAccessibleQuickWidgetOffscreenWindow::childCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleQuickWidgetOffscreenWindow::indexOfChild(const
//      QAccessibleInterface *iface) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK37QAccessibleQuickWidgetOffscreenWindow12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWidgetOffscreenWindow *self,
    const QAccessibleInterface *iface) {
  return self->QAccessibleQuickWidgetOffscreenWindow::indexOfChild(iface);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
