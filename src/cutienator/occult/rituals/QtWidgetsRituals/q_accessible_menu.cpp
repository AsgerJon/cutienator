//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qaccessiblemenu_p.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(menubar)
#include <QtWidgets/qmenubar.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qwidget_p.h>
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

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 47, as _ZNK15QAccessibleMenu10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenu::childCount() const
{
    return menu()->actions().size();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 60, as _ZNK15QAccessibleMenu4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QString QAccessibleMenu::text(QAccessible::Text t) const
{
    QString tx = QAccessibleWidgetV2::text(t);
    if (!tx.isEmpty())
        return tx;

    if (t == QAccessible::Name)
        return menu()->windowTitle();
    return tx;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 71, as _ZNK15QAccessibleMenu4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessible::Role QAccessibleMenu::role() const
{
    return QAccessible::PopupMenu;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 105, as _ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenu::indexOfChild( const QAccessibleInterface *child) const
{
    QAccessible::Role r = child->role();
    if ((r == QAccessible::MenuItem || r == QAccessible::Separator) && menu()) {
        return menu()->actions().indexOf(qobject_cast<QAction*>(child->object()));
    }
    return -1;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 42, as _ZNK15QAccessibleMenu4menuEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QMenu *QAccessibleMenu::menu() const
{
    return qobject_cast<QMenu*>(object());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMenu that Python can take functions over in. Every QAccessibleMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall0)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef QString * (*CuteQAccessibleMenuCall2)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall3)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall4)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall5)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall6)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleMenuCall7)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleMenuCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleMenuCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleMenuCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuCall18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMenu : public QAccessibleMenu {
public:
  using QAccessibleMenu::QAccessibleMenu;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
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
#if QT_CONFIG(menu)
  //  int QAccessibleMenu::childCount() const
  int childCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMenuCall0 call = reinterpret_cast<CuteQAccessibleMenuCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMenu::childCount();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMenuCall1 call = reinterpret_cast<CuteQAccessibleMenuCall1>(taken[1]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::childAt(x, y);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QString QAccessibleMenu::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleMenuCall2 call = reinterpret_cast<CuteQAccessibleMenuCall2>(taken[2]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleMenu::text(t);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessible::Role QAccessibleMenu::role() const
  QAccessible::Role role() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleMenuCall3 call = reinterpret_cast<CuteQAccessibleMenuCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleMenu::role();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleMenuCall4 call = reinterpret_cast<CuteQAccessibleMenuCall4>(taken[4]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::child(index);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleMenuCall5 call = reinterpret_cast<CuteQAccessibleMenuCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::parent();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
  //      const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleMenuCall6 call = reinterpret_cast<CuteQAccessibleMenuCall6>(taken[6]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleMenu::indexOfChild(child);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleMenuCall7 call = reinterpret_cast<CuteQAccessibleMenuCall7>(taken[7]);
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
      CuteQAccessibleMenuCall8 call = reinterpret_cast<CuteQAccessibleMenuCall8>(taken[8]);
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
      CuteQAccessibleMenuCall9 call = reinterpret_cast<CuteQAccessibleMenuCall9>(taken[9]);
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
      CuteQAccessibleMenuCall10 call = reinterpret_cast<CuteQAccessibleMenuCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleMenuCall11 call = reinterpret_cast<CuteQAccessibleMenuCall11>(taken[11]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleMenuCall12 call = reinterpret_cast<CuteQAccessibleMenuCall12>(taken[12]);
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
      CuteQAccessibleMenuCall13 call = reinterpret_cast<CuteQAccessibleMenuCall13>(taken[13]);
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
      CuteQAccessibleMenuCall14 call = reinterpret_cast<CuteQAccessibleMenuCall14>(taken[14]);
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
      CuteQAccessibleMenuCall15 call = reinterpret_cast<CuteQAccessibleMenuCall15>(taken[15]);
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
      CuteQAccessibleMenuCall16 call = reinterpret_cast<CuteQAccessibleMenuCall16>(taken[16]);
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
      CuteQAccessibleMenuCall17 call = reinterpret_cast<CuteQAccessibleMenuCall17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleMenuCall18 call = reinterpret_cast<CuteQAccessibleMenuCall18>(taken[18]);
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
      CuteQAccessibleMenuCall19 call = reinterpret_cast<CuteQAccessibleMenuCall19>(taken[19]);
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

//  int QAccessibleMenu::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleMenu10childCountEv(const QAccessibleMenu *self) {
  return self->childCount();
}

//  QString QAccessibleMenu::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAccessibleMenu4textEN11QAccessible4TextE(
    const QAccessibleMenu *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleMenu::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QAccessibleMenu4roleEv(
    const QAccessibleMenu *self) {
  return self->role();
}

//  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenu *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QMenu *QAccessibleMenu::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK15QAccessibleMenu4menuEv(const QAccessibleMenu *self) {
  return self->menu();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleMenu, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMenu(
    QAccessibleMenu *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMenu *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenu::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleMenu10childCountEv(
    const QAccessibleMenu *self) {
  return self->QAccessibleMenu::childCount();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QString QAccessibleMenu::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QAccessibleMenu4textEN11QAccessible4TextE(
    const QAccessibleMenu *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleMenu::text(t));
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessible::Role QAccessibleMenu::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QAccessibleMenu4roleEv(
    const QAccessibleMenu *self) {
  return self->QAccessibleMenu::role();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenu *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleMenu::indexOfChild(child);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
