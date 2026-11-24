//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertysheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerPropertySheet that Python can take functions over in. Every QDesignerPropertySheet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerPropertySheetCall0)(const void *, const QString *, int *);
typedef int (*CuteQDesignerPropertySheetCall1)(const void *, int *);
typedef QString * (*CuteQDesignerPropertySheetCall2)(const void *, int, int *);
typedef QString * (*CuteQDesignerPropertySheetCall3)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetCall4)(const void *, int, const QString *, int *);
typedef bool (*CuteQDesignerPropertySheetCall5)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetCall6)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetCall7)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetCall8)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerPropertySheetCall9)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetCall10)(const void *, int, bool, int *);
typedef const QVariant * (*CuteQDesignerPropertySheetCall11)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetCall12)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQDesignerPropertySheetCall13)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetCall14)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerPropertySheetCall15)(const void *, int *);
typedef int (*CuteQDesignerPropertySheetCall16)(const void *, const QString *, const QVariant *, int *);
typedef bool (*CuteQDesignerPropertySheetCall17)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetCall18)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetCall19)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerPropertySheetCall20)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPropertySheetCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPropertySheetCall22)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertySheetCall23)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertySheetCall24)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertySheetCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertySheetCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertySheetCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerPropertySheet : public QDesignerPropertySheet {
public:
  using QDesignerPropertySheet::QDesignerPropertySheet;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension5countEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension12propertyNameEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension13propertyGroupEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension16setPropertyGroupEiRK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension8hasResetEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension5resetEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension11isAttributeEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension12setAttributeEib")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isVisibleEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension10setVisibleEib")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension8propertyEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension11setPropertyEiRK8QVariant")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isChangedEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension10setChangedEib")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension24dynamicPropertiesAllowedEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension18addDynamicPropertyERK7QStringRK8QVariant")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPropertyEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicPropertyEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicPropertyERK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isEnabledEi")) {
      taken[20] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QDesignerPropertySheet::indexOf(const QString &name) const
  int indexOf(const QString &name) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall0 call = reinterpret_cast<CuteQDesignerPropertySheetCall0>(taken[0]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::indexOf(name);
  }

  //  int QDesignerPropertySheet::count() const
  int count() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall1 call = reinterpret_cast<CuteQDesignerPropertySheetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::count();
  }

  //  QString QDesignerPropertySheet::propertyName(int index) const
  QString propertyName(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall2 call = reinterpret_cast<CuteQDesignerPropertySheetCall2>(taken[2]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerPropertySheet::propertyName(index);
  }

  //  QString QDesignerPropertySheet::propertyGroup(int index) const
  QString propertyGroup(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall3 call = reinterpret_cast<CuteQDesignerPropertySheetCall3>(taken[3]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerPropertySheet::propertyGroup(index);
  }

  //  void QDesignerPropertySheet::setPropertyGroup(int index, const
  //      QString &group)
  void setPropertyGroup(int index, const QString &group) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall4 call = reinterpret_cast<CuteQDesignerPropertySheetCall4>(taken[4]);
      call(this, index, &group, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setPropertyGroup(index, group);
  }

  //  bool QDesignerPropertySheet::hasReset(int index) const
  bool hasReset(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall5 call = reinterpret_cast<CuteQDesignerPropertySheetCall5>(taken[5]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::hasReset(index);
  }

  //  bool QDesignerPropertySheet::reset(int index)
  bool reset(int index) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall6 call = reinterpret_cast<CuteQDesignerPropertySheetCall6>(taken[6]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::reset(index);
  }

  //  bool QDesignerPropertySheet::isAttribute(int index) const
  bool isAttribute(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall7 call = reinterpret_cast<CuteQDesignerPropertySheetCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isAttribute(index);
  }

  //  void QDesignerPropertySheet::setAttribute(int index, bool b)
  void setAttribute(int index, bool b) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall8 call = reinterpret_cast<CuteQDesignerPropertySheetCall8>(taken[8]);
      call(this, index, b, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setAttribute(index, b);
  }

  //  bool QDesignerPropertySheet::isVisible(int index) const
  bool isVisible(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall9 call = reinterpret_cast<CuteQDesignerPropertySheetCall9>(taken[9]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isVisible(index);
  }

  //  void QDesignerPropertySheet::setVisible(int index, bool b)
  void setVisible(int index, bool b) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall10 call = reinterpret_cast<CuteQDesignerPropertySheetCall10>(taken[10]);
      call(this, index, b, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setVisible(index, b);
  }

  //  QVariant QDesignerPropertySheet::property(int index) const
  QVariant property(int index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall11 call = reinterpret_cast<CuteQDesignerPropertySheetCall11>(taken[11]);
      const QVariant * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QDesignerPropertySheet::property(index);
  }

  //  void QDesignerPropertySheet::setProperty(int index, const QVariant
  //      &value)
  void setProperty(int index, const QVariant &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall12 call = reinterpret_cast<CuteQDesignerPropertySheetCall12>(taken[12]);
      call(this, index, &value, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setProperty(index, value);
  }

  //  bool QDesignerPropertySheet::isChanged(int index) const
  bool isChanged(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall13 call = reinterpret_cast<CuteQDesignerPropertySheetCall13>(taken[13]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isChanged(index);
  }

  //  void QDesignerPropertySheet::setChanged(int index, bool changed)
  void setChanged(int index, bool changed) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall14 call = reinterpret_cast<CuteQDesignerPropertySheetCall14>(taken[14]);
      call(this, index, changed, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setChanged(index, changed);
  }

  //  bool QDesignerPropertySheet::dynamicPropertiesAllowed() const
  bool dynamicPropertiesAllowed() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall15 call = reinterpret_cast<CuteQDesignerPropertySheetCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::dynamicPropertiesAllowed();
  }

  //  int QDesignerPropertySheet::addDynamicProperty(const QString
  //      &propertyName, const QVariant &value)
  int addDynamicProperty(
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall16 call = reinterpret_cast<CuteQDesignerPropertySheetCall16>(taken[16]);
      int given = call(this, &propertyName, &value, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::addDynamicProperty(propertyName, value);
  }

  //  bool QDesignerPropertySheet::removeDynamicProperty(int index)
  bool removeDynamicProperty(int index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall17 call = reinterpret_cast<CuteQDesignerPropertySheetCall17>(taken[17]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::removeDynamicProperty(index);
  }

  //  bool QDesignerPropertySheet::isDynamicProperty(int index) const
  bool isDynamicProperty(int index) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall18 call = reinterpret_cast<CuteQDesignerPropertySheetCall18>(taken[18]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isDynamicProperty(index);
  }

  //  bool QDesignerPropertySheet::canAddDynamicProperty(const QString
  //      &propertyName) const
  bool canAddDynamicProperty(const QString &propertyName) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall19 call = reinterpret_cast<CuteQDesignerPropertySheetCall19>(taken[19]);
      bool given = call(this, &propertyName, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::canAddDynamicProperty(propertyName);
  }

  //  bool QDesignerPropertySheet::isEnabled(int index) const
  bool isEnabled(int index) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall20 call = reinterpret_cast<CuteQDesignerPropertySheetCall20>(taken[20]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isEnabled(index);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall21 call = reinterpret_cast<CuteQDesignerPropertySheetCall21>(taken[21]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall22 call = reinterpret_cast<CuteQDesignerPropertySheetCall22>(taken[22]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall23 call = reinterpret_cast<CuteQDesignerPropertySheetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall24 call = reinterpret_cast<CuteQDesignerPropertySheetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall25 call = reinterpret_cast<CuteQDesignerPropertySheetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall26 call = reinterpret_cast<CuteQDesignerPropertySheetCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerPropertySheetCall27 call = reinterpret_cast<CuteQDesignerPropertySheetCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerPropertySheet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDesignerPropertySheet10metaObjectEv(
    const QDesignerPropertySheet *self) {
  return self->metaObject();
}

//  QString QDesignerPropertySheet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QDesignerPropertySheet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerPropertySheet::tr(s, c, n));
}

//  QDesignerPropertySheet::QDesignerPropertySheet(QObject *object, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDesignerPropertySheet *ritual_ZN22QDesignerPropertySheetC1EP7QObjectS1_(
    QObject *object,
    QObject *parent) {
  return new CuteQDesignerPropertySheet(object, parent);
}

//  QDesignerPropertySheet::~QDesignerPropertySheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheetD1Ev(QDesignerPropertySheet *self) {
  delete self;
}

//  int QDesignerPropertySheet::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDesignerPropertySheet7indexOfERK7QString(
    const QDesignerPropertySheet *self,
    const QString *name) {
  return self->indexOf(*name);
}

//  int QDesignerPropertySheet::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDesignerPropertySheet5countEv(
    const QDesignerPropertySheet *self) {
  return self->count();
}

//  QString QDesignerPropertySheet::propertyName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDesignerPropertySheet12propertyNameEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QString(self->propertyName(index));
}

//  QString QDesignerPropertySheet::propertyGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDesignerPropertySheet13propertyGroupEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QString(self->propertyGroup(index));
}

//  void QDesignerPropertySheet::setPropertyGroup(int index, const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet16setPropertyGroupEiRK7QString(
    QDesignerPropertySheet *self,
    int index,
    const QString *group) {
  self->setPropertyGroup(index, *group);
}

//  bool QDesignerPropertySheet::hasReset(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet8hasResetEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->hasReset(index);
}

//  bool QDesignerPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDesignerPropertySheet5resetEi(
    QDesignerPropertySheet *self,
    int index) {
  return self->reset(index);
}

//  bool QDesignerPropertySheet::isAttribute(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet11isAttributeEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isAttribute(index);
}

//  void QDesignerPropertySheet::setAttribute(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet12setAttributeEib(
    QDesignerPropertySheet *self,
    int index,
    bool b) {
  self->setAttribute(index, b);
}

//  bool QDesignerPropertySheet::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet9isVisibleEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isVisible(index);
}

//  void QDesignerPropertySheet::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet10setVisibleEib(
    QDesignerPropertySheet *self,
    int index,
    bool b) {
  self->setVisible(index, b);
}

//  QVariant QDesignerPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QDesignerPropertySheet8propertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QVariant(self->property(index));
}

//  void QDesignerPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet11setPropertyEiRK8QVariant(
    QDesignerPropertySheet *self,
    int index,
    const QVariant *value) {
  self->setProperty(index, *value);
}

//  bool QDesignerPropertySheet::isChanged(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet9isChangedEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isChanged(index);
}

//  void QDesignerPropertySheet::setChanged(int index, bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet10setChangedEib(
    QDesignerPropertySheet *self,
    int index,
    bool changed) {
  self->setChanged(index, changed);
}

//  bool QDesignerPropertySheet::dynamicPropertiesAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet24dynamicPropertiesAllowedEv(
    const QDesignerPropertySheet *self) {
  return self->dynamicPropertiesAllowed();
}

//  int QDesignerPropertySheet::addDynamicProperty(const QString
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDesignerPropertySheet18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerPropertySheet *self,
    const QString *propertyName,
    const QVariant *value) {
  return self->addDynamicProperty(*propertyName, *value);
}

//  bool QDesignerPropertySheet::removeDynamicProperty(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDesignerPropertySheet21removeDynamicPropertyEi(
    QDesignerPropertySheet *self,
    int index) {
  return self->removeDynamicProperty(index);
}

//  bool QDesignerPropertySheet::isDynamicProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet17isDynamicPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isDynamicProperty(index);
}

//  bool QDesignerPropertySheet::canAddDynamicProperty(const QString
//      &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet21canAddDynamicPropertyERK7QString(
    const QDesignerPropertySheet *self,
    const QString *propertyName) {
  return self->canAddDynamicProperty(*propertyName);
}

//  bool QDesignerPropertySheet::isDefaultDynamicProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet24isDefaultDynamicPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isDefaultDynamicProperty(index);
}

//  bool QDesignerPropertySheet::isResourceProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet18isResourcePropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isResourceProperty(index);
}

//  QVariant QDesignerPropertySheet::defaultResourceProperty(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QDesignerPropertySheet23defaultResourcePropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QVariant(self->defaultResourceProperty(index));
}

//  qdesigner_internal::DesignerPixmapCache
//      *QDesignerPropertySheet::pixmapCache() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerPixmapCache *ritual_ZNK22QDesignerPropertySheet11pixmapCacheEv(
    const QDesignerPropertySheet *self) {
  return self->pixmapCache();
}

//  void QDesignerPropertySheet::setPixmapCache(qdesigner_internal::DesignerP
//      ixmapCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet14setPixmapCacheEPN18qdesigner_internal19DesignerPixmapCacheE(
    QDesignerPropertySheet *self,
    qdesigner_internal::DesignerPixmapCache *cache) {
  self->setPixmapCache(cache);
}

//  qdesigner_internal::DesignerIconCache
//      *QDesignerPropertySheet::iconCache() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DesignerIconCache *ritual_ZNK22QDesignerPropertySheet9iconCacheEv(
    const QDesignerPropertySheet *self) {
  return self->iconCache();
}

//  void QDesignerPropertySheet::setIconCache(qdesigner_internal::DesignerIco
//      nCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet12setIconCacheEPN18qdesigner_internal17DesignerIconCacheE(
    QDesignerPropertySheet *self,
    qdesigner_internal::DesignerIconCache *cache) {
  self->setIconCache(cache);
}

//  int QDesignerPropertySheet::createFakeProperty(const QString
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDesignerPropertySheet18createFakePropertyERK7QStringRK8QVariant(
    QDesignerPropertySheet *self,
    const QString *propertyName,
    const QVariant *value) {
  return self->createFakeProperty(*propertyName, *value);
}

//  bool QDesignerPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet9isEnabledEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isEnabled(index);
}

//  QObject *QDesignerPropertySheet::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QDesignerPropertySheet6objectEv(
    const QDesignerPropertySheet *self) {
  return self->object();
}

//  bool QDesignerPropertySheet::internalDynamicPropertiesEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDesignerPropertySheet32internalDynamicPropertiesEnabledEv() {
  return QDesignerPropertySheet::internalDynamicPropertiesEnabled();
}

//  void QDesignerPropertySheet::setInternalDynamicPropertiesEnabled(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet35setInternalDynamicPropertiesEnabledEb(
    bool v) {
  QDesignerPropertySheet::setInternalDynamicPropertiesEnabled(v);
}

//  QDesignerFormEditorInterface
//      *QDesignerPropertySheet::formEditorForObject(QObject *o)
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZN22QDesignerPropertySheet19formEditorForObjectEP7QObject(
    QObject *o) {
  return QDesignerPropertySheet::formEditorForObject(o);
}

//  bool QDesignerPropertySheet::isAdditionalProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet20isAdditionalPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isAdditionalProperty(index);
}

//  bool QDesignerPropertySheet::isFakeProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet14isFakePropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isFakeProperty(index);
}

//  QVariant QDesignerPropertySheet::resolvePropertyValue(int index, const
//      QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QDesignerPropertySheet20resolvePropertyValueEiRK8QVariant(
    const QDesignerPropertySheet *self,
    int index,
    const QVariant *value) {
  return new QVariant(self->resolvePropertyValue(index, *value));
}

//  QVariant QDesignerPropertySheet::metaProperty(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QDesignerPropertySheet12metaPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QVariant(self->metaProperty(index));
}

//  void QDesignerPropertySheet::setFakeProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet15setFakePropertyEiRK8QVariant(
    QDesignerPropertySheet *self,
    int index,
    const QVariant *value) {
  self->setFakeProperty(index, *value);
}

//  void QDesignerPropertySheet::clearFakeProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDesignerPropertySheet19clearFakePropertiesEv(
    QDesignerPropertySheet *self) {
  self->clearFakeProperties();
}

//  bool QDesignerPropertySheet::isFakeLayoutProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet20isFakeLayoutPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isFakeLayoutProperty(index);
}

//  bool QDesignerPropertySheet::isDynamic(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDesignerPropertySheet9isDynamicEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->isDynamic(index);
}

//  qdesigner_internal::FormWindowBase
//      *QDesignerPropertySheet::formWindowBase() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::FormWindowBase *ritual_ZNK22QDesignerPropertySheet14formWindowBaseEv(
    const QDesignerPropertySheet *self) {
  return self->formWindowBase();
}

//  QDesignerFormEditorInterface *QDesignerPropertySheet::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK22QDesignerPropertySheet4coreEv(
    const QDesignerPropertySheet *self) {
  return self->core();
}

//  ObjectType QDesignerPropertySheet::objectTypeFromObject(const QObject *o)
extern "C" Q_DECL_EXPORT
QDesignerPropertySheet::ObjectType ritual_ZN22QDesignerPropertySheet20objectTypeFromObjectEPK7QObject(
    const QObject *o) {
  return QDesignerPropertySheet::objectTypeFromObject(o);
}

//  ObjectFlags QDesignerPropertySheet::objectFlagsFromObject(const QObject
//      *o)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDesignerPropertySheet21objectFlagsFromObjectEPK7QObject(
    const QObject *o) {
  return static_cast<int>(
      QDesignerPropertySheet::objectFlagsFromObject(
          o).toInt());
}

//  PropertyType QDesignerPropertySheet::propertyTypeFromName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QDesignerPropertySheet::PropertyType ritual_ZN22QDesignerPropertySheet20propertyTypeFromNameERK7QString(
    const QString *name) {
  return QDesignerPropertySheet::propertyTypeFromName(*name);
}

//  PropertyType QDesignerPropertySheet::propertyType(int index) const
extern "C" Q_DECL_EXPORT
QDesignerPropertySheet::PropertyType ritual_ZNK22QDesignerPropertySheet12propertyTypeEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->propertyType(index);
}

//  ObjectType QDesignerPropertySheet::objectType() const
extern "C" Q_DECL_EXPORT
QDesignerPropertySheet::ObjectType ritual_ZNK22QDesignerPropertySheet10objectTypeEv(
    const QDesignerPropertySheet *self) {
  return self->objectType();
}

//  QDesignerPropertySheet as the QDesignerPropertySheetExtension it is built
//      on
extern "C" Q_DECL_EXPORT
QDesignerPropertySheetExtension *ritual_cast_QDesignerPropertySheet_QDesignerPropertySheetExtension(
    QDesignerPropertySheet *self) {
  return static_cast<QDesignerPropertySheetExtension *>(self);
}

//  QDesignerPropertySheet as the QDesignerDynamicPropertySheetExtension it
//      is built on
extern "C" Q_DECL_EXPORT
QDesignerDynamicPropertySheetExtension *ritual_cast_QDesignerPropertySheet_QDesignerDynamicPropertySheetExtension(
    QDesignerPropertySheet *self) {
  return static_cast<QDesignerDynamicPropertySheetExtension *>(self);
}

//  a Python function taken by a CuteQDesignerPropertySheet, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerPropertySheet(
    QDesignerPropertySheet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerPropertySheet *>(self)->take(key, call);
}

//  int QDesignerPropertySheet::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QDesignerPropertySheet7indexOfERK7QString(
    const QDesignerPropertySheet *self,
    const QString *name) {
  return self->QDesignerPropertySheet::indexOf(*name);
}

//  int QDesignerPropertySheet::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QDesignerPropertySheet5countEv(
    const QDesignerPropertySheet *self) {
  return self->QDesignerPropertySheet::count();
}

//  QString QDesignerPropertySheet::propertyName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QDesignerPropertySheet12propertyNameEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QString(self->QDesignerPropertySheet::propertyName(index));
}

//  QString QDesignerPropertySheet::propertyGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK22QDesignerPropertySheet13propertyGroupEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QString(self->QDesignerPropertySheet::propertyGroup(index));
}

//  void QDesignerPropertySheet::setPropertyGroup(int index, const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDesignerPropertySheet16setPropertyGroupEiRK7QString(
    QDesignerPropertySheet *self,
    int index,
    const QString *group) {
  self->QDesignerPropertySheet::setPropertyGroup(index, *group);
}

//  bool QDesignerPropertySheet::hasReset(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet8hasResetEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::hasReset(index);
}

//  bool QDesignerPropertySheet::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QDesignerPropertySheet5resetEi(
    QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::reset(index);
}

//  bool QDesignerPropertySheet::isAttribute(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet11isAttributeEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::isAttribute(index);
}

//  void QDesignerPropertySheet::setAttribute(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDesignerPropertySheet12setAttributeEib(
    QDesignerPropertySheet *self,
    int index,
    bool b) {
  self->QDesignerPropertySheet::setAttribute(index, b);
}

//  bool QDesignerPropertySheet::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet9isVisibleEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::isVisible(index);
}

//  void QDesignerPropertySheet::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDesignerPropertySheet10setVisibleEib(
    QDesignerPropertySheet *self,
    int index,
    bool b) {
  self->QDesignerPropertySheet::setVisible(index, b);
}

//  QVariant QDesignerPropertySheet::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QDesignerPropertySheet8propertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return new QVariant(self->QDesignerPropertySheet::property(index));
}

//  void QDesignerPropertySheet::setProperty(int index, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDesignerPropertySheet11setPropertyEiRK8QVariant(
    QDesignerPropertySheet *self,
    int index,
    const QVariant *value) {
  self->QDesignerPropertySheet::setProperty(index, *value);
}

//  bool QDesignerPropertySheet::isChanged(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet9isChangedEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::isChanged(index);
}

//  void QDesignerPropertySheet::setChanged(int index, bool changed)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDesignerPropertySheet10setChangedEib(
    QDesignerPropertySheet *self,
    int index,
    bool changed) {
  self->QDesignerPropertySheet::setChanged(index, changed);
}

//  bool QDesignerPropertySheet::dynamicPropertiesAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet24dynamicPropertiesAllowedEv(
    const QDesignerPropertySheet *self) {
  return self->QDesignerPropertySheet::dynamicPropertiesAllowed();
}

//  int QDesignerPropertySheet::addDynamicProperty(const QString
//      &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN22QDesignerPropertySheet18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerPropertySheet *self,
    const QString *propertyName,
    const QVariant *value) {
  return self->QDesignerPropertySheet::addDynamicProperty(
      *propertyName,
      *value);
}

//  bool QDesignerPropertySheet::removeDynamicProperty(int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QDesignerPropertySheet21removeDynamicPropertyEi(
    QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::removeDynamicProperty(index);
}

//  bool QDesignerPropertySheet::isDynamicProperty(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet17isDynamicPropertyEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::isDynamicProperty(index);
}

//  bool QDesignerPropertySheet::canAddDynamicProperty(const QString
//      &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet21canAddDynamicPropertyERK7QString(
    const QDesignerPropertySheet *self,
    const QString *propertyName) {
  return self->QDesignerPropertySheet::canAddDynamicProperty(*propertyName);
}

//  bool QDesignerPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QDesignerPropertySheet9isEnabledEi(
    const QDesignerPropertySheet *self,
    int index) {
  return self->QDesignerPropertySheet::isEnabled(index);
}
