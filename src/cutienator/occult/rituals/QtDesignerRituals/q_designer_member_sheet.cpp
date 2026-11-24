//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_membersheet_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_membersheet_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerMemberSheet that Python can take functions over in. Every QDesignerMemberSheet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerMemberSheetCall0)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMemberSheetCall1)(const void *, int *);
typedef QString * (*CuteQDesignerMemberSheetCall2)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetCall3)(const void *, int, int *);
typedef void (*CuteQDesignerMemberSheetCall4)(const void *, int, const QString *, int *);
typedef bool (*CuteQDesignerMemberSheetCall5)(const void *, int, int *);
typedef void (*CuteQDesignerMemberSheetCall6)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerMemberSheetCall7)(const void *, int, int *);
typedef bool (*CuteQDesignerMemberSheetCall8)(const void *, int, int *);
typedef bool (*CuteQDesignerMemberSheetCall9)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetCall10)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetCall11)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMemberSheetCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerMemberSheetCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerMemberSheetCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerMemberSheet : public QDesignerMemberSheet {
public:
  using QDesignerMemberSheet::QDesignerMemberSheet;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension7indexOfERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension5countEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension10memberNameEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension11memberGroupEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerMemberSheetExtension14setMemberGroupEiRK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension9isVisibleEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerMemberSheetExtension10setVisibleEib")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension8isSignalEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension6isSlotEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension19inheritedFromWidgetEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension15declaredInClassEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension9signatureEi")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QDesignerMemberSheet::indexOf(const QString &name) const
  int indexOf(const QString &name) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall0 call = reinterpret_cast<CuteQDesignerMemberSheetCall0>(taken[0]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::indexOf(name);
  }

  //  int QDesignerMemberSheet::count() const
  int count() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall1 call = reinterpret_cast<CuteQDesignerMemberSheetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::count();
  }

  //  QString QDesignerMemberSheet::memberName(int index) const
  QString memberName(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall2 call = reinterpret_cast<CuteQDesignerMemberSheetCall2>(taken[2]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerMemberSheet::memberName(index);
  }

  //  QString QDesignerMemberSheet::memberGroup(int index) const
  QString memberGroup(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall3 call = reinterpret_cast<CuteQDesignerMemberSheetCall3>(taken[3]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerMemberSheet::memberGroup(index);
  }

  //  void QDesignerMemberSheet::setMemberGroup(int index, const QString
  //      &group)
  void setMemberGroup(int index, const QString &group) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall4 call = reinterpret_cast<CuteQDesignerMemberSheetCall4>(taken[4]);
      call(this, index, &group, &handled);
      if (handled) return;
    }
    QDesignerMemberSheet::setMemberGroup(index, group);
  }

  //  bool QDesignerMemberSheet::isVisible(int index) const
  bool isVisible(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall5 call = reinterpret_cast<CuteQDesignerMemberSheetCall5>(taken[5]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::isVisible(index);
  }

  //  void QDesignerMemberSheet::setVisible(int index, bool b)
  void setVisible(int index, bool b) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall6 call = reinterpret_cast<CuteQDesignerMemberSheetCall6>(taken[6]);
      call(this, index, b, &handled);
      if (handled) return;
    }
    QDesignerMemberSheet::setVisible(index, b);
  }

  //  bool QDesignerMemberSheet::isSignal(int index) const
  bool isSignal(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall7 call = reinterpret_cast<CuteQDesignerMemberSheetCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::isSignal(index);
  }

  //  bool QDesignerMemberSheet::isSlot(int index) const
  bool isSlot(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall8 call = reinterpret_cast<CuteQDesignerMemberSheetCall8>(taken[8]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::isSlot(index);
  }

  //  bool QDesignerMemberSheet::inheritedFromWidget(int index) const
  bool inheritedFromWidget(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall9 call = reinterpret_cast<CuteQDesignerMemberSheetCall9>(taken[9]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return QDesignerMemberSheet::inheritedFromWidget(index);
  }

  //  QString QDesignerMemberSheet::declaredInClass(int index) const
  QString declaredInClass(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall10 call = reinterpret_cast<CuteQDesignerMemberSheetCall10>(taken[10]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerMemberSheet::declaredInClass(index);
  }

  //  QString QDesignerMemberSheet::signature(int index) const
  QString signature(int index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall11 call = reinterpret_cast<CuteQDesignerMemberSheetCall11>(taken[11]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerMemberSheet::signature(index);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall12 call = reinterpret_cast<CuteQDesignerMemberSheetCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall13 call = reinterpret_cast<CuteQDesignerMemberSheetCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall14 call = reinterpret_cast<CuteQDesignerMemberSheetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall15 call = reinterpret_cast<CuteQDesignerMemberSheetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall16 call = reinterpret_cast<CuteQDesignerMemberSheetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall17 call = reinterpret_cast<CuteQDesignerMemberSheetCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerMemberSheetCall18 call = reinterpret_cast<CuteQDesignerMemberSheetCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerMemberSheet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDesignerMemberSheet10metaObjectEv(
    const QDesignerMemberSheet *self) {
  return self->metaObject();
}

//  QString QDesignerMemberSheet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDesignerMemberSheet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerMemberSheet::tr(s, c, n));
}

//  QDesignerMemberSheet::QDesignerMemberSheet(QObject *object, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDesignerMemberSheet *ritual_ZN20QDesignerMemberSheetC1EP7QObjectS1_(
    QObject *object,
    QObject *parent) {
  return new CuteQDesignerMemberSheet(object, parent);
}

//  QDesignerMemberSheet::~QDesignerMemberSheet()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerMemberSheetD1Ev(QDesignerMemberSheet *self) {
  delete self;
}

//  int QDesignerMemberSheet::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDesignerMemberSheet7indexOfERK7QString(
    const QDesignerMemberSheet *self,
    const QString *name) {
  return self->indexOf(*name);
}

//  int QDesignerMemberSheet::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDesignerMemberSheet5countEv(
    const QDesignerMemberSheet *self) {
  return self->count();
}

//  QString QDesignerMemberSheet::memberName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerMemberSheet10memberNameEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->memberName(index));
}

//  QString QDesignerMemberSheet::memberGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerMemberSheet11memberGroupEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->memberGroup(index));
}

//  void QDesignerMemberSheet::setMemberGroup(int index, const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerMemberSheet14setMemberGroupEiRK7QString(
    QDesignerMemberSheet *self,
    int index,
    const QString *group) {
  self->setMemberGroup(index, *group);
}

//  bool QDesignerMemberSheet::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesignerMemberSheet9isVisibleEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->isVisible(index);
}

//  void QDesignerMemberSheet::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerMemberSheet10setVisibleEib(
    QDesignerMemberSheet *self,
    int index,
    bool b) {
  self->setVisible(index, b);
}

//  bool QDesignerMemberSheet::isSignal(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesignerMemberSheet8isSignalEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->isSignal(index);
}

//  bool QDesignerMemberSheet::isSlot(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesignerMemberSheet6isSlotEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->isSlot(index);
}

//  bool QDesignerMemberSheet::inheritedFromWidget(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesignerMemberSheet19inheritedFromWidgetEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->inheritedFromWidget(index);
}

//  bool QDesignerMemberSheet::signalMatchesSlot(const QString &signal, const
//      QString &slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QDesignerMemberSheet17signalMatchesSlotERK7QStringS2_(
    const QString *signal,
    const QString *slot) {
  return QDesignerMemberSheet::signalMatchesSlot(*signal, *slot);
}

//  QString QDesignerMemberSheet::declaredInClass(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerMemberSheet15declaredInClassEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->declaredInClass(index));
}

//  QString QDesignerMemberSheet::signature(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerMemberSheet9signatureEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->signature(index));
}

//  QList<QByteArray> QDesignerMemberSheet::parameterTypes(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK20QDesignerMemberSheet14parameterTypesEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QList<QByteArray>(self->parameterTypes(index));
}

//  QList<QByteArray> QDesignerMemberSheet::parameterNames(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK20QDesignerMemberSheet14parameterNamesEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QList<QByteArray>(self->parameterNames(index));
}

//  QDesignerMemberSheet as the QDesignerMemberSheetExtension it is built on
extern "C" Q_DECL_EXPORT
QDesignerMemberSheetExtension *ritual_cast_QDesignerMemberSheet_QDesignerMemberSheetExtension(
    QDesignerMemberSheet *self) {
  return static_cast<QDesignerMemberSheetExtension *>(self);
}

//  a Python function taken by a CuteQDesignerMemberSheet, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMemberSheet(
    QDesignerMemberSheet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMemberSheet *>(self)->take(key, call);
}

//  int QDesignerMemberSheet::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QDesignerMemberSheet7indexOfERK7QString(
    const QDesignerMemberSheet *self,
    const QString *name) {
  return self->QDesignerMemberSheet::indexOf(*name);
}

//  int QDesignerMemberSheet::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QDesignerMemberSheet5countEv(
    const QDesignerMemberSheet *self) {
  return self->QDesignerMemberSheet::count();
}

//  QString QDesignerMemberSheet::memberName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerMemberSheet10memberNameEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->QDesignerMemberSheet::memberName(index));
}

//  QString QDesignerMemberSheet::memberGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerMemberSheet11memberGroupEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->QDesignerMemberSheet::memberGroup(index));
}

//  void QDesignerMemberSheet::setMemberGroup(int index, const QString
//      &group)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerMemberSheet14setMemberGroupEiRK7QString(
    QDesignerMemberSheet *self,
    int index,
    const QString *group) {
  self->QDesignerMemberSheet::setMemberGroup(index, *group);
}

//  bool QDesignerMemberSheet::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesignerMemberSheet9isVisibleEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->QDesignerMemberSheet::isVisible(index);
}

//  void QDesignerMemberSheet::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerMemberSheet10setVisibleEib(
    QDesignerMemberSheet *self,
    int index,
    bool b) {
  self->QDesignerMemberSheet::setVisible(index, b);
}

//  bool QDesignerMemberSheet::isSignal(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesignerMemberSheet8isSignalEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->QDesignerMemberSheet::isSignal(index);
}

//  bool QDesignerMemberSheet::isSlot(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesignerMemberSheet6isSlotEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->QDesignerMemberSheet::isSlot(index);
}

//  bool QDesignerMemberSheet::inheritedFromWidget(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesignerMemberSheet19inheritedFromWidgetEi(
    const QDesignerMemberSheet *self,
    int index) {
  return self->QDesignerMemberSheet::inheritedFromWidget(index);
}

//  QString QDesignerMemberSheet::declaredInClass(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerMemberSheet15declaredInClassEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->QDesignerMemberSheet::declaredInClass(index));
}

//  QString QDesignerMemberSheet::signature(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerMemberSheet9signatureEi(
    const QDesignerMemberSheet *self,
    int index) {
  return new QString(self->QDesignerMemberSheet::signature(index));
}
