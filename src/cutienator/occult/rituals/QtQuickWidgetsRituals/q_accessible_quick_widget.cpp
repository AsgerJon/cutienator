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
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
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

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 12, as _ZN22QAccessibleQuickWidgetC1EP12QQuickWidget
#if QT_CONFIG(accessibility)
inline QAccessibleQuickWidget::QAccessibleQuickWidget(QQuickWidget* widget)
    : QAccessibleWidgetV2(widget)
{
    // NOTE: m_accessibleWindow is a QAccessibleQuickWindow, and not a
    // QAccessibleQuickWidgetOffscreenWindow (defined below). This means
    // it will return the Quick item child interfaces, which is what's needed here
    // (unlike QAccessibleQuickWidgetOffscreenWindow, which will report 0 children).
    repairWindow();
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 22, as _ZN22QAccessibleQuickWidgetD1Ev
#if QT_CONFIG(accessibility)
inline QAccessibleQuickWidget::~QAccessibleQuickWidget()
{
    QObject::disconnect(m_connection);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 42, as _ZNK22QAccessibleQuickWidget5childEi
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleQuickWidget::child(int index) const
{
    return m_accessibleWindow->child(index);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 47, as _ZNK22QAccessibleQuickWidget10childCountEv
#if QT_CONFIG(accessibility)
inline int QAccessibleQuickWidget::childCount() const
{
    return m_accessibleWindow->childCount();
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 52, as _ZNK22QAccessibleQuickWidget12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
inline int QAccessibleQuickWidget::indexOfChild(const QAccessibleInterface *iface) const
{
    return m_accessibleWindow->indexOfChild(iface);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 57, as _ZNK22QAccessibleQuickWidget7childAtEii
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QAccessibleQuickWidget::childAt(int x, int y) const
{
    return m_accessibleWindow->childAt(x, y);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quickwidgets/qaccessiblequickwidget.cpp, line 27, as _ZN22QAccessibleQuickWidget12repairWindowEv
#if QT_CONFIG(accessibility)
inline void QAccessibleQuickWidget::repairWindow()
{
    if (!m_accessibleWindow || !m_accessibleWindow->object()) {
        QQuickWidget *theWidget = static_cast<QQuickWidget *>(object());
        QQuickWindow *newOffscreen = QQuickWidgetPrivate::get(theWidget)->offscreenWindow;
        // We use the qobject_cast here to detect that the newOffscreen is
        // not the one getting destroyed right now.
        if (qobject_cast<QQuickWindow *>(newOffscreen)) {
            m_accessibleWindow.reset(new QAccessibleQuickWindow(newOffscreen));
            m_connection = QObject::connect(newOffscreen, &QObject::destroyed, theWidget,
                                            [this] { repairWindow(); });
        }
    }
}
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleQuickWidget that Python can take functions over in. Every QAccessibleQuickWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall4)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickWidgetCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickWidgetCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickWidgetCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickWidgetCall11)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickWidgetCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleQuickWidgetCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickWidgetCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickWidgetCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickWidgetCall16)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickWidgetCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickWidgetCall18)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickWidgetCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickWidgetCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickWidgetCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleQuickWidget : public QAccessibleQuickWidget {
public:
  using QAccessibleQuickWidget::QAccessibleQuickWidget;
  void *taken[22] = {};

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
  //  QAccessibleInterface *QAccessibleQuickWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetCall0 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickWidget::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetCall1 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickWidget::indexOfChild(const QAccessibleInterface
  //      *iface) const
  int indexOfChild(const QAccessibleInterface *iface) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetCall2 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall2>(taken[2]);
      int given = call(this, iface, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickWidget::indexOfChild(iface);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickWidget::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetCall3 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall3>(taken[3]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickWidget::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleQuickWidgetCall4 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall4>(taken[4]);
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
      CuteQAccessibleQuickWidgetCall5 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall5>(taken[5]);
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
      CuteQAccessibleQuickWidgetCall6 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall6>(taken[6]);
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
      CuteQAccessibleQuickWidgetCall7 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall7>(taken[7]);
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
      CuteQAccessibleQuickWidgetCall8 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall8>(taken[8]);
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
      CuteQAccessibleQuickWidgetCall9 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall9>(taken[9]);
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
      CuteQAccessibleQuickWidgetCall10 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall10>(taken[10]);
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
      CuteQAccessibleQuickWidgetCall11 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall11>(taken[11]);
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
      CuteQAccessibleQuickWidgetCall12 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall12>(taken[12]);
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
      CuteQAccessibleQuickWidgetCall13 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall13>(taken[13]);
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
      CuteQAccessibleQuickWidgetCall14 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall14>(taken[14]);
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
      CuteQAccessibleQuickWidgetCall15 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall15>(taken[15]);
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
      CuteQAccessibleQuickWidgetCall16 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall16>(taken[16]);
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
      CuteQAccessibleQuickWidgetCall17 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall17>(taken[17]);
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
      CuteQAccessibleQuickWidgetCall18 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall18>(taken[18]);
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
      CuteQAccessibleQuickWidgetCall19 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall19>(taken[19]);
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
      CuteQAccessibleQuickWidgetCall20 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall20>(taken[20]);
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
      CuteQAccessibleQuickWidgetCall21 call = reinterpret_cast<CuteQAccessibleQuickWidgetCall21>(taken[21]);
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
//  QAccessibleQuickWidget::QAccessibleQuickWidget(QQuickWidget *widget)
extern "C" Q_DECL_EXPORT
QAccessibleQuickWidget *ritual_ZN22QAccessibleQuickWidgetC1EP12QQuickWidget(
    QQuickWidget *widget) {
  return new CuteQAccessibleQuickWidget(widget);
}
#endif  // QT_CONFIG(accessibility)

//  QAccessibleQuickWidget::~QAccessibleQuickWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAccessibleQuickWidgetD1Ev(QAccessibleQuickWidget *self) {
  delete self;
}

//  QAccessibleInterface *QAccessibleQuickWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWidget5childEi(
    const QAccessibleQuickWidget *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleQuickWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleQuickWidget10childCountEv(
    const QAccessibleQuickWidget *self) {
  return self->childCount();
}

//  int QAccessibleQuickWidget::indexOfChild(const QAccessibleInterface
//      *iface) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAccessibleQuickWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWidget *self,
    const QAccessibleInterface *iface) {
  return self->indexOfChild(iface);
}

//  QAccessibleInterface *QAccessibleQuickWidget::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK22QAccessibleQuickWidget7childAtEii(
    const QAccessibleQuickWidget *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

#if QT_CONFIG(accessibility)
//  void QAccessibleQuickWidget::repairWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAccessibleQuickWidget12repairWindowEv(
    QAccessibleQuickWidget *self) {
  self->repairWindow();
}
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleQuickWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleQuickWidget(
    QAccessibleQuickWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleQuickWidget *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleQuickWidget::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWidget5childEi(
    const QAccessibleQuickWidget *self,
    int index) {
  return self->QAccessibleQuickWidget::child(index);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleQuickWidget::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleQuickWidget10childCountEv(
    const QAccessibleQuickWidget *self) {
  return self->QAccessibleQuickWidget::childCount();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  int QAccessibleQuickWidget::indexOfChild(const QAccessibleInterface
//      *iface) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QAccessibleQuickWidget12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickWidget *self,
    const QAccessibleInterface *iface) {
  return self->QAccessibleQuickWidget::indexOfChild(iface);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QAccessibleQuickWidget::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK22QAccessibleQuickWidget7childAtEii(
    const QAccessibleQuickWidget *self,
    int x,
    int y) {
  return self->QAccessibleQuickWidget::childAt(x, y);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
