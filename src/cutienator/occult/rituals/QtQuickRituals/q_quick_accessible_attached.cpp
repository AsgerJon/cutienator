//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickaccessibleattached_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickaccessibleattached_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickAccessibleAttached that Python can take functions over in. Every QQuickAccessibleAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAccessibleAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAccessibleAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAccessibleAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAccessibleAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAccessibleAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAccessibleAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAccessibleAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAccessibleAttached : public QQuickAccessibleAttached {
public:
  using QQuickAccessibleAttached::QQuickAccessibleAttached;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall0 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall1 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall2 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall3 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall4 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall5 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAccessibleAttachedCall6 call = reinterpret_cast<CuteQQuickAccessibleAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAccessibleAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickAccessibleAttached10metaObjectEv(
    const QQuickAccessibleAttached *self) {
  return self->metaObject();
}

//  QString QQuickAccessibleAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickAccessibleAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAccessibleAttached::tr(s, c, n));
}

//  void QQuickAccessibleAttached::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached24qt_qmlMarker_uncreatableEv(
    QQuickAccessibleAttached *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickAccessibleAttached::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached21qt_qmlMarker_attachedEv(
    QQuickAccessibleAttached *self) {
  self->qt_qmlMarker_attached();
}

//  const QMetaObject *QQuickAccessibleAttached::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN24QQuickAccessibleAttached20qmlExtendedNamespaceEv() {
  return QQuickAccessibleAttached::qmlExtendedNamespace();
}

//  void QQuickAccessibleAttached::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached30qt_qmlMarker_extendedNamespaceEv(
    QQuickAccessibleAttached *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  bool QQuickAccessibleAttached::checkable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached9checkableEv(
    const QQuickAccessibleAttached *self) {
  return self->checkable();
}

//  void QQuickAccessibleAttached::set_checkable(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached13set_checkableEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_checkable(arg);
}

//  bool QQuickAccessibleAttached::checked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached7checkedEv(
    const QQuickAccessibleAttached *self) {
  return self->checked();
}

//  void QQuickAccessibleAttached::set_checked(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached11set_checkedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_checked(arg);
}

//  bool QQuickAccessibleAttached::editable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached8editableEv(
    const QQuickAccessibleAttached *self) {
  return self->editable();
}

//  void QQuickAccessibleAttached::set_editable(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached12set_editableEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_editable(arg);
}

//  bool QQuickAccessibleAttached::expandable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached10expandableEv(
    const QQuickAccessibleAttached *self) {
  return self->expandable();
}

//  void QQuickAccessibleAttached::set_expandable(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached14set_expandableEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_expandable(arg);
}

//  bool QQuickAccessibleAttached::expanded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached8expandedEv(
    const QQuickAccessibleAttached *self) {
  return self->expanded();
}

//  void QQuickAccessibleAttached::set_expanded(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached12set_expandedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_expanded(arg);
}

//  bool QQuickAccessibleAttached::focusable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached9focusableEv(
    const QQuickAccessibleAttached *self) {
  return self->focusable();
}

//  void QQuickAccessibleAttached::set_focusable(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached13set_focusableEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_focusable(arg);
}

//  bool QQuickAccessibleAttached::focused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached7focusedEv(
    const QQuickAccessibleAttached *self) {
  return self->focused();
}

//  void QQuickAccessibleAttached::set_focused(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached11set_focusedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_focused(arg);
}

//  bool QQuickAccessibleAttached::multiLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached9multiLineEv(
    const QQuickAccessibleAttached *self) {
  return self->multiLine();
}

//  void QQuickAccessibleAttached::set_multiLine(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached13set_multiLineEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_multiLine(arg);
}

//  bool QQuickAccessibleAttached::readOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached8readOnlyEv(
    const QQuickAccessibleAttached *self) {
  return self->readOnly();
}

//  void QQuickAccessibleAttached::set_readOnly(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached12set_readOnlyEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_readOnly(arg);
}

//  bool QQuickAccessibleAttached::selected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached8selectedEv(
    const QQuickAccessibleAttached *self) {
  return self->selected();
}

//  void QQuickAccessibleAttached::set_selected(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached12set_selectedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_selected(arg);
}

//  bool QQuickAccessibleAttached::selectable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached10selectableEv(
    const QQuickAccessibleAttached *self) {
  return self->selectable();
}

//  void QQuickAccessibleAttached::set_selectable(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached14set_selectableEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_selectable(arg);
}

//  bool QQuickAccessibleAttached::pressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached7pressedEv(
    const QQuickAccessibleAttached *self) {
  return self->pressed();
}

//  void QQuickAccessibleAttached::set_pressed(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached11set_pressedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_pressed(arg);
}

//  bool QQuickAccessibleAttached::checkStateMixed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached15checkStateMixedEv(
    const QQuickAccessibleAttached *self) {
  return self->checkStateMixed();
}

//  void QQuickAccessibleAttached::set_checkStateMixed(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached19set_checkStateMixedEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_checkStateMixed(arg);
}

//  bool QQuickAccessibleAttached::defaultButton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached13defaultButtonEv(
    const QQuickAccessibleAttached *self) {
  return self->defaultButton();
}

//  void QQuickAccessibleAttached::set_defaultButton(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached17set_defaultButtonEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_defaultButton(arg);
}

//  bool QQuickAccessibleAttached::passwordEdit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached12passwordEditEv(
    const QQuickAccessibleAttached *self) {
  return self->passwordEdit();
}

//  void QQuickAccessibleAttached::set_passwordEdit(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached16set_passwordEditEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_passwordEdit(arg);
}

//  bool QQuickAccessibleAttached::selectableText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached14selectableTextEv(
    const QQuickAccessibleAttached *self) {
  return self->selectableText();
}

//  void QQuickAccessibleAttached::set_selectableText(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached18set_selectableTextEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_selectableText(arg);
}

//  bool QQuickAccessibleAttached::searchEdit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached10searchEditEv(
    const QQuickAccessibleAttached *self) {
  return self->searchEdit();
}

//  void QQuickAccessibleAttached::set_searchEdit(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached14set_searchEditEb(
    QQuickAccessibleAttached *self,
    bool arg) {
  self->set_searchEdit(arg);
}

//  QQuickAccessibleAttached::QQuickAccessibleAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAccessibleAttached *ritual_ZN24QQuickAccessibleAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickAccessibleAttached(parent);
}

//  QQuickAccessibleAttached::~QQuickAccessibleAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttachedD1Ev(
    QQuickAccessibleAttached *self) {
  delete self;
}

//  QAccessible::Role QQuickAccessibleAttached::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK24QQuickAccessibleAttached4roleEv(
    const QQuickAccessibleAttached *self) {
  return self->role();
}

//  void QQuickAccessibleAttached::setRole(QAccessible::Role role)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached7setRoleEN11QAccessible4RoleE(
    QQuickAccessibleAttached *self,
    QAccessible::Role role) {
  self->setRole(role);
}

//  QString QQuickAccessibleAttached::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickAccessibleAttached4nameEv(
    const QQuickAccessibleAttached *self) {
  return new QString(self->name());
}

//  bool QQuickAccessibleAttached::wasNameExplicitlySet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached20wasNameExplicitlySetEv(
    const QQuickAccessibleAttached *self) {
  return self->wasNameExplicitlySet();
}

//  void QQuickAccessibleAttached::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached7setNameERK7QString(
    QQuickAccessibleAttached *self,
    const QString *name) {
  self->setName(*name);
}

//  void QQuickAccessibleAttached::setNameImplicitly(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached17setNameImplicitlyERK7QString(
    QQuickAccessibleAttached *self,
    const QString *name) {
  self->setNameImplicitly(*name);
}

//  QString QQuickAccessibleAttached::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickAccessibleAttached11descriptionEv(
    const QQuickAccessibleAttached *self) {
  return new QString(self->description());
}

//  void QQuickAccessibleAttached::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached14setDescriptionERK7QString(
    QQuickAccessibleAttached *self,
    const QString *description) {
  self->setDescription(*description);
}

//  void QQuickAccessibleAttached::setDescriptionImplicitly(const QString
//      &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached24setDescriptionImplicitlyERK7QString(
    QQuickAccessibleAttached *self,
    const QString *desc) {
  self->setDescriptionImplicitly(*desc);
}

//  QString QQuickAccessibleAttached::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickAccessibleAttached2idEv(
    const QQuickAccessibleAttached *self) {
  return new QString(self->id());
}

//  void QQuickAccessibleAttached::setId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached5setIdERK7QString(
    QQuickAccessibleAttached *self,
    const QString *id) {
  self->setId(*id);
}

//  QQuickItem *QQuickAccessibleAttached::labelledBy() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickAccessibleAttached10labelledByEv(
    const QQuickAccessibleAttached *self) {
  return self->labelledBy();
}

//  void QQuickAccessibleAttached::setLabelledBy(QQuickItem *labelledBy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached13setLabelledByEP10QQuickItem(
    QQuickAccessibleAttached *self,
    QQuickItem *labelledBy) {
  self->setLabelledBy(labelledBy);
}

//  void QQuickAccessibleAttached::setLabelledByInternal(QQuickItem
//      *labelledBy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached21setLabelledByInternalEP10QQuickItem(
    QQuickAccessibleAttached *self,
    QQuickItem *labelledBy) {
  self->setLabelledByInternal(labelledBy);
}

//  QQuickItem *QQuickAccessibleAttached::labelFor() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickAccessibleAttached8labelForEv(
    const QQuickAccessibleAttached *self) {
  return self->labelFor();
}

//  void QQuickAccessibleAttached::setLabelFor(QQuickItem *labelFor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached11setLabelForEP10QQuickItem(
    QQuickAccessibleAttached *self,
    QQuickItem *labelFor) {
  self->setLabelFor(labelFor);
}

//  void QQuickAccessibleAttached::setLabelForInternal(QQuickItem *labelFor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached19setLabelForInternalEP10QQuickItem(
    QQuickAccessibleAttached *self,
    QQuickItem *labelFor) {
  self->setLabelForInternal(labelFor);
}

//  QQuickAccessibleAttached
//      *QQuickAccessibleAttached::qmlAttachedProperties(QObject *obj)
extern "C" Q_DECL_EXPORT
QQuickAccessibleAttached *ritual_ZN24QQuickAccessibleAttached21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQuickAccessibleAttached::qmlAttachedProperties(obj);
}

//  QQuickAccessibleAttached
//      *QQuickAccessibleAttached::attachedProperties(const QObject *obj)
extern "C" Q_DECL_EXPORT
QQuickAccessibleAttached *ritual_ZN24QQuickAccessibleAttached18attachedPropertiesEPK7QObject(
    const QObject *obj) {
  return QQuickAccessibleAttached::attachedProperties(obj);
}

//  QVariant QQuickAccessibleAttached::property(const QObject *object, const
//      char *propertyName)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN24QQuickAccessibleAttached8propertyEPK7QObjectPKc(
    const QObject *object,
    const char *propertyName) {
  return new QVariant(
      QQuickAccessibleAttached::property(
          object,
          propertyName));
}

//  bool QQuickAccessibleAttached::setProperty(QObject *object, const char
//      *propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickAccessibleAttached11setPropertyEP7QObjectPKcRK8QVariant(
    QObject *object,
    const char *propertyName,
    const QVariant *value) {
  return QQuickAccessibleAttached::setProperty(object, propertyName, *value);
}

//  QObject *QQuickAccessibleAttached::findAccessible(QObject *object,
//      QAccessible::Role role)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN24QQuickAccessibleAttached14findAccessibleEP7QObjectN11QAccessible4RoleE(
    QObject *object,
    QAccessible::Role role) {
  return QQuickAccessibleAttached::findAccessible(object, role);
}

//  QAccessible::State QQuickAccessibleAttached::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK24QQuickAccessibleAttached5stateEv(
    const QQuickAccessibleAttached *self) {
  return new QAccessible::State(self->state());
}

//  bool QQuickAccessibleAttached::ignored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAccessibleAttached7ignoredEv(
    const QQuickAccessibleAttached *self) {
  return self->ignored();
}

//  bool QQuickAccessibleAttached::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickAccessibleAttached8doActionERK7QString(
    QQuickAccessibleAttached *self,
    const QString *actionName) {
  return self->doAction(*actionName);
}

//  QString QQuickAccessibleAttached::stripHtml(const QString &html)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickAccessibleAttached9stripHtmlERK7QString(
    const QString *html) {
  return new QString(QQuickAccessibleAttached::stripHtml(*html));
}

//  void QQuickAccessibleAttached::setProxying(QQuickAccessibleAttached
//      *proxying)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached11setProxyingEPS_(
    QQuickAccessibleAttached *self,
    QQuickAccessibleAttached *proxying) {
  self->setProxying(proxying);
}

//  void QQuickAccessibleAttached::announce(const QString &message,
//      QAccessible::AnnouncementPoliteness politeness)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached8announceERK7QStringN11QAccessible22AnnouncementPolitenessE(
    QQuickAccessibleAttached *self,
    const QString *message,
    QAccessible::AnnouncementPoliteness politeness) {
  self->announce(*message, politeness);
}

//  void QQuickAccessibleAttached::valueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached12valueChangedEv(
    QQuickAccessibleAttached *self) {
  self->valueChanged();
}

//  void QQuickAccessibleAttached::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached21cursorPositionChangedEv(
    QQuickAccessibleAttached *self) {
  self->cursorPositionChanged();
}

//  void QQuickAccessibleAttached::setIgnored(bool ignored)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAccessibleAttached10setIgnoredEb(
    QQuickAccessibleAttached *self,
    bool ignored) {
  self->setIgnored(ignored);
}

//  QQuickItem *QQuickAccessibleAttached::findRelation(QAccessible::Relation
//      relation) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickAccessibleAttached12findRelationE6QFlagsIN11QAccessible12RelationFlagEE(
    const QQuickAccessibleAttached *self,
    int relation) {
  return self->findRelation(
      QFlags<QAccessible::RelationFlag>::fromInt(relation));
}

//  a Python function taken by a CuteQQuickAccessibleAttached, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAccessibleAttached(
    QQuickAccessibleAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAccessibleAttached *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
