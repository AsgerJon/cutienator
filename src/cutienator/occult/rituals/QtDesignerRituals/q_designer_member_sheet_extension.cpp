//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/membersheet.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/membersheet.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerMemberSheetExtension that Python can take functions over in. Every QDesignerMemberSheetExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerMemberSheetExtensionCall0)(const void *, int *);
typedef int (*CuteQDesignerMemberSheetExtensionCall1)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerMemberSheetExtensionCall2)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetExtensionCall3)(const void *, int, int *);
typedef void (*CuteQDesignerMemberSheetExtensionCall4)(const void *, int, const QString *, int *);
typedef bool (*CuteQDesignerMemberSheetExtensionCall5)(const void *, int, int *);
typedef void (*CuteQDesignerMemberSheetExtensionCall6)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerMemberSheetExtensionCall7)(const void *, int, int *);
typedef bool (*CuteQDesignerMemberSheetExtensionCall8)(const void *, int, int *);
typedef bool (*CuteQDesignerMemberSheetExtensionCall9)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetExtensionCall10)(const void *, int, int *);
typedef QString * (*CuteQDesignerMemberSheetExtensionCall11)(const void *, int, int *);
class CuteQDesignerMemberSheetExtension : public QDesignerMemberSheetExtension {
public:
  using QDesignerMemberSheetExtension::QDesignerMemberSheetExtension;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerMemberSheetExtension7indexOfERK7QString")) {
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
    return false;
  }

  //  int QDesignerMemberSheetExtension::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall0 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMemberSheetExtension::indexOf(const QString &name) const
  int indexOf(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall1 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall1>(taken[1]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMemberSheetExtension::memberName(int index) const
  QString memberName(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall2 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall2>(taken[2]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMemberSheetExtension::memberGroup(int index) const
  QString memberGroup(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall3 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall3>(taken[3]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerMemberSheetExtension::setMemberGroup(int index, const
  //      QString &group)
  void setMemberGroup(int index, const QString &group) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall4 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall4>(taken[4]);
      call(this, index, &group, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerMemberSheetExtension::isVisible(int index) const
  bool isVisible(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall5 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall5>(taken[5]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerMemberSheetExtension::setVisible(int index, bool b)
  void setVisible(int index, bool b) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall6 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall6>(taken[6]);
      call(this, index, b, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerMemberSheetExtension::isSignal(int index) const
  bool isSignal(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall7 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerMemberSheetExtension::isSlot(int index) const
  bool isSlot(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall8 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall8>(taken[8]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerMemberSheetExtension::inheritedFromWidget(int index)
  //      const
  bool inheritedFromWidget(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall9 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall9>(taken[9]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMemberSheetExtension::declaredInClass(int index)
  //      const
  QString declaredInClass(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall10 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall10>(taken[10]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMemberSheetExtension::signature(int index) const
  QString signature(int index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMemberSheetExtensionCall11 call = reinterpret_cast<CuteQDesignerMemberSheetExtensionCall11>(taken[11]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QDesignerMemberSheetExtension::~QDesignerMemberSheetExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerMemberSheetExtensionD1Ev(
    QDesignerMemberSheetExtension *self) {
  delete self;
}

//  int QDesignerMemberSheetExtension::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDesignerMemberSheetExtension5countEv(
    const QDesignerMemberSheetExtension *self) {
  return self->count();
}

//  int QDesignerMemberSheetExtension::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDesignerMemberSheetExtension7indexOfERK7QString(
    const QDesignerMemberSheetExtension *self,
    const QString *name) {
  return self->indexOf(*name);
}

//  QString QDesignerMemberSheetExtension::memberName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerMemberSheetExtension10memberNameEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QString(self->memberName(index));
}

//  QString QDesignerMemberSheetExtension::memberGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerMemberSheetExtension11memberGroupEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QString(self->memberGroup(index));
}

//  void QDesignerMemberSheetExtension::setMemberGroup(int index, const
//      QString &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerMemberSheetExtension14setMemberGroupEiRK7QString(
    QDesignerMemberSheetExtension *self,
    int index,
    const QString *group) {
  self->setMemberGroup(index, *group);
}

//  bool QDesignerMemberSheetExtension::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerMemberSheetExtension9isVisibleEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return self->isVisible(index);
}

//  void QDesignerMemberSheetExtension::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerMemberSheetExtension10setVisibleEib(
    QDesignerMemberSheetExtension *self,
    int index,
    bool b) {
  self->setVisible(index, b);
}

//  bool QDesignerMemberSheetExtension::isSignal(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerMemberSheetExtension8isSignalEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return self->isSignal(index);
}

//  bool QDesignerMemberSheetExtension::isSlot(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerMemberSheetExtension6isSlotEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return self->isSlot(index);
}

//  bool QDesignerMemberSheetExtension::inheritedFromWidget(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDesignerMemberSheetExtension19inheritedFromWidgetEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return self->inheritedFromWidget(index);
}

//  QString QDesignerMemberSheetExtension::declaredInClass(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerMemberSheetExtension15declaredInClassEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QString(self->declaredInClass(index));
}

//  QString QDesignerMemberSheetExtension::signature(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerMemberSheetExtension9signatureEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QString(self->signature(index));
}

//  QList<QByteArray> QDesignerMemberSheetExtension::parameterTypes(int
//      index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK29QDesignerMemberSheetExtension14parameterTypesEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QList<QByteArray>(self->parameterTypes(index));
}

//  QList<QByteArray> QDesignerMemberSheetExtension::parameterNames(int
//      index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK29QDesignerMemberSheetExtension14parameterNamesEi(
    const QDesignerMemberSheetExtension *self,
    int index) {
  return new QList<QByteArray>(self->parameterNames(index));
}

//  a Python function taken by a CuteQDesignerMemberSheetExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMemberSheetExtension(
    QDesignerMemberSheetExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMemberSheetExtension *>(self)->take(key, call);
}
