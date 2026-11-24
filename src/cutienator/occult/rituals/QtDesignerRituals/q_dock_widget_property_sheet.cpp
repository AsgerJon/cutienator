//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dockwidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_dockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDockWidgetPropertySheet that Python can take functions over in. Every QDockWidgetPropertySheet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDockWidgetPropertySheetCall0)(const void *, int, int *);
typedef int (*CuteQDockWidgetPropertySheetCall1)(const void *, const QString *, int *);
typedef int (*CuteQDockWidgetPropertySheetCall2)(const void *, int *);
typedef QString * (*CuteQDockWidgetPropertySheetCall3)(const void *, int, int *);
typedef QString * (*CuteQDockWidgetPropertySheetCall4)(const void *, int, int *);
typedef void (*CuteQDockWidgetPropertySheetCall5)(const void *, int, const QString *, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall6)(const void *, int, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall7)(const void *, int, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall8)(const void *, int, int *);
typedef void (*CuteQDockWidgetPropertySheetCall9)(const void *, int, bool, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall10)(const void *, int, int *);
typedef void (*CuteQDockWidgetPropertySheetCall11)(const void *, int, bool, int *);
typedef const QVariant * (*CuteQDockWidgetPropertySheetCall12)(const void *, int, int *);
typedef void (*CuteQDockWidgetPropertySheetCall13)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall14)(const void *, int, int *);
typedef void (*CuteQDockWidgetPropertySheetCall15)(const void *, int, bool, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall16)(const void *, int *);
typedef int (*CuteQDockWidgetPropertySheetCall17)(const void *, const QString *, const QVariant *, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall18)(const void *, int, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall19)(const void *, int, int *);
typedef bool (*CuteQDockWidgetPropertySheetCall20)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDockWidgetPropertySheetCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDockWidgetPropertySheetCall22)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetPropertySheetCall23)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetPropertySheetCall24)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetPropertySheetCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetPropertySheetCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDockWidgetPropertySheetCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDockWidgetPropertySheet : public QDockWidgetPropertySheet {
public:
  using QDockWidgetPropertySheet::QDockWidgetPropertySheet;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isEnabledEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension5countEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension12propertyNameEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension13propertyGroupEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension16setPropertyGroupEiRK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension8hasResetEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension5resetEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension11isAttributeEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension12setAttributeEib")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isVisibleEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension10setVisibleEib")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension8propertyEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension11setPropertyEiRK8QVariant")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isChangedEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension10setChangedEib")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension24dynamicPropertiesAllowedEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension18addDynamicPropertyERK7QStringRK8QVariant")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPropertyEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicPropertyEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicPropertyERK7QString")) {
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

  //  bool QDockWidgetPropertySheet::isEnabled(int index) const
  bool isEnabled(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall0 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall0>(taken[0]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDockWidgetPropertySheet::isEnabled(index);
  }

  //  int QDesignerPropertySheet::indexOf(const QString &name) const
  int indexOf(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall1 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall1>(taken[1]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::indexOf(name);
  }

  //  int QDesignerPropertySheet::count() const
  int count() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall2 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::count();
  }

  //  QString QDesignerPropertySheet::propertyName(int index) const
  QString propertyName(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall3 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall4 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall5 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall5>(taken[5]);
      call(this, index, &group, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setPropertyGroup(index, group);
  }

  //  bool QDesignerPropertySheet::hasReset(int index) const
  bool hasReset(int index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall6 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall6>(taken[6]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::hasReset(index);
  }

  //  bool QDesignerPropertySheet::reset(int index)
  bool reset(int index) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall7 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::reset(index);
  }

  //  bool QDesignerPropertySheet::isAttribute(int index) const
  bool isAttribute(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall8 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall8>(taken[8]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isAttribute(index);
  }

  //  void QDesignerPropertySheet::setAttribute(int index, bool b)
  void setAttribute(int index, bool b) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall9 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall9>(taken[9]);
      call(this, index, b, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setAttribute(index, b);
  }

  //  bool QDesignerPropertySheet::isVisible(int index) const
  bool isVisible(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall10 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall10>(taken[10]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isVisible(index);
  }

  //  void QDesignerPropertySheet::setVisible(int index, bool b)
  void setVisible(int index, bool b) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall11 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall11>(taken[11]);
      call(this, index, b, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setVisible(index, b);
  }

  //  QVariant QDesignerPropertySheet::property(int index) const
  QVariant property(int index) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall12 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall12>(taken[12]);
      const QVariant * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QDesignerPropertySheet::property(index);
  }

  //  void QDesignerPropertySheet::setProperty(int index, const QVariant
  //      &value)
  void setProperty(int index, const QVariant &value) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall13 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall13>(taken[13]);
      call(this, index, &value, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setProperty(index, value);
  }

  //  bool QDesignerPropertySheet::isChanged(int index) const
  bool isChanged(int index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall14 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall14>(taken[14]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isChanged(index);
  }

  //  void QDesignerPropertySheet::setChanged(int index, bool changed)
  void setChanged(int index, bool changed) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall15 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall15>(taken[15]);
      call(this, index, changed, &handled);
      if (handled) return;
    }
    QDesignerPropertySheet::setChanged(index, changed);
  }

  //  bool QDesignerPropertySheet::dynamicPropertiesAllowed() const
  bool dynamicPropertiesAllowed() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall16 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall17 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall17>(taken[17]);
      int given = call(this, &propertyName, &value, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::addDynamicProperty(propertyName, value);
  }

  //  bool QDesignerPropertySheet::removeDynamicProperty(int index)
  bool removeDynamicProperty(int index) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall18 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall18>(taken[18]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::removeDynamicProperty(index);
  }

  //  bool QDesignerPropertySheet::isDynamicProperty(int index) const
  bool isDynamicProperty(int index) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall19 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall19>(taken[19]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::isDynamicProperty(index);
  }

  //  bool QDesignerPropertySheet::canAddDynamicProperty(const QString
  //      &propertyName) const
  bool canAddDynamicProperty(const QString &propertyName) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall20 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall20>(taken[20]);
      bool given = call(this, &propertyName, &handled);
      if (handled) return given;
    }
    return QDesignerPropertySheet::canAddDynamicProperty(propertyName);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDockWidgetPropertySheetCall21 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall21>(taken[21]);
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
      CuteQDockWidgetPropertySheetCall22 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall22>(taken[22]);
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
      CuteQDockWidgetPropertySheetCall23 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall23>(taken[23]);
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
      CuteQDockWidgetPropertySheetCall24 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall24>(taken[24]);
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
      CuteQDockWidgetPropertySheetCall25 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall25>(taken[25]);
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
      CuteQDockWidgetPropertySheetCall26 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall26>(taken[26]);
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
      CuteQDockWidgetPropertySheetCall27 call = reinterpret_cast<CuteQDockWidgetPropertySheetCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDockWidgetPropertySheet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QDockWidgetPropertySheet10metaObjectEv(
    const QDockWidgetPropertySheet *self) {
  return self->metaObject();
}

//  QString QDockWidgetPropertySheet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QDockWidgetPropertySheet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDockWidgetPropertySheet::tr(s, c, n));
}

//  bool QDockWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QDockWidgetPropertySheet9isEnabledEi(
    const QDockWidgetPropertySheet *self,
    int index) {
  return self->isEnabled(index);
}

//  a Python function taken by a CuteQDockWidgetPropertySheet, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDockWidgetPropertySheet(
    QDockWidgetPropertySheet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDockWidgetPropertySheet *>(self)->take(key, call);
}

//  bool QDockWidgetPropertySheet::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QDockWidgetPropertySheet9isEnabledEi(
    const QDockWidgetPropertySheet *self,
    int index) {
  return self->QDockWidgetPropertySheet::isEnabled(index);
}
