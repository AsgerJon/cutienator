//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/propertysheet.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/propertysheet.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QDesignerPropertySheetExtension that Python can take functions over in. Every QDesignerPropertySheetExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerPropertySheetExtensionCall0)(const void *, int *);
typedef int (*CuteQDesignerPropertySheetExtensionCall1)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerPropertySheetExtensionCall2)(const void *, int, int *);
typedef QString * (*CuteQDesignerPropertySheetExtensionCall3)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetExtensionCall4)(const void *, int, const QString *, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall5)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall6)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall7)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetExtensionCall8)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall9)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetExtensionCall10)(const void *, int, bool, int *);
typedef const QVariant * (*CuteQDesignerPropertySheetExtensionCall11)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetExtensionCall12)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall13)(const void *, int, int *);
typedef void (*CuteQDesignerPropertySheetExtensionCall14)(const void *, int, bool, int *);
typedef bool (*CuteQDesignerPropertySheetExtensionCall15)(const void *, int, int *);
class CuteQDesignerPropertySheetExtension : public QDesignerPropertySheetExtension {
public:
  using QDesignerPropertySheetExtension::QDesignerPropertySheetExtension;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension5countEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString")) {
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
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isVisibleEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension10setVisibleEib")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension11isAttributeEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN31QDesignerPropertySheetExtension12setAttributeEib")) {
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
    if (!std::strcmp(key, "_ZNK31QDesignerPropertySheetExtension9isEnabledEi")) {
      taken[15] = call;
      return true;
    }
    return false;
  }

  //  int QDesignerPropertySheetExtension::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall0 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerPropertySheetExtension::indexOf(const QString &name)
  //      const
  int indexOf(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall1 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall1>(taken[1]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerPropertySheetExtension::propertyName(int index)
  //      const
  QString propertyName(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall2 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall2>(taken[2]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerPropertySheetExtension::propertyGroup(int index)
  //      const
  QString propertyGroup(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall3 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall3>(taken[3]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerPropertySheetExtension::setPropertyGroup(int index,
  //      const QString &group)
  void setPropertyGroup(int index, const QString &group) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall4 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall4>(taken[4]);
      call(this, index, &group, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerPropertySheetExtension::hasReset(int index) const
  bool hasReset(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall5 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall5>(taken[5]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerPropertySheetExtension::reset(int index)
  bool reset(int index) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall6 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall6>(taken[6]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerPropertySheetExtension::isVisible(int index) const
  bool isVisible(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall7 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall7>(taken[7]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerPropertySheetExtension::setVisible(int index, bool b)
  void setVisible(int index, bool b) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall8 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall8>(taken[8]);
      call(this, index, b, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerPropertySheetExtension::isAttribute(int index) const
  bool isAttribute(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall9 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall9>(taken[9]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerPropertySheetExtension::setAttribute(int index, bool b)
  void setAttribute(int index, bool b) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall10 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall10>(taken[10]);
      call(this, index, b, &handled);
      if (handled) return;
    }
  }

  //  QVariant QDesignerPropertySheetExtension::property(int index) const
  QVariant property(int index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall11 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall11>(taken[11]);
      const QVariant * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerPropertySheetExtension::setProperty(int index, const
  //      QVariant &value)
  void setProperty(int index, const QVariant &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall12 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall12>(taken[12]);
      call(this, index, &value, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerPropertySheetExtension::isChanged(int index) const
  bool isChanged(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall13 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall13>(taken[13]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerPropertySheetExtension::setChanged(int index, bool
  //      changed)
  void setChanged(int index, bool changed) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall14 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall14>(taken[14]);
      call(this, index, changed, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerPropertySheetExtension::isEnabled(int index) const
  bool isEnabled(int index) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerPropertySheetExtensionCall15 call = reinterpret_cast<CuteQDesignerPropertySheetExtensionCall15>(taken[15]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDesignerPropertySheetExtension::QDesignerPropertySheetExtension()
extern "C" Q_DECL_EXPORT
QDesignerPropertySheetExtension *ritual_ZN31QDesignerPropertySheetExtensionC1Ev() {
  return new CuteQDesignerPropertySheetExtension();
}

//  QDesignerPropertySheetExtension::~QDesignerPropertySheetExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtensionD1Ev(
    QDesignerPropertySheetExtension *self) {
  delete self;
}

//  int QDesignerPropertySheetExtension::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QDesignerPropertySheetExtension5countEv(
    const QDesignerPropertySheetExtension *self) {
  return self->count();
}

//  int QDesignerPropertySheetExtension::indexOf(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString(
    const QDesignerPropertySheetExtension *self,
    const QString *name) {
  return self->indexOf(*name);
}

//  QString QDesignerPropertySheetExtension::propertyName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QDesignerPropertySheetExtension12propertyNameEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return new QString(self->propertyName(index));
}

//  QString QDesignerPropertySheetExtension::propertyGroup(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QDesignerPropertySheetExtension13propertyGroupEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return new QString(self->propertyGroup(index));
}

//  void QDesignerPropertySheetExtension::setPropertyGroup(int index, const
//      QString &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtension16setPropertyGroupEiRK7QString(
    QDesignerPropertySheetExtension *self,
    int index,
    const QString *group) {
  self->setPropertyGroup(index, *group);
}

//  bool QDesignerPropertySheetExtension::hasReset(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerPropertySheetExtension8hasResetEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return self->hasReset(index);
}

//  bool QDesignerPropertySheetExtension::reset(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QDesignerPropertySheetExtension5resetEi(
    QDesignerPropertySheetExtension *self,
    int index) {
  return self->reset(index);
}

//  bool QDesignerPropertySheetExtension::isVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerPropertySheetExtension9isVisibleEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return self->isVisible(index);
}

//  void QDesignerPropertySheetExtension::setVisible(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtension10setVisibleEib(
    QDesignerPropertySheetExtension *self,
    int index,
    bool b) {
  self->setVisible(index, b);
}

//  bool QDesignerPropertySheetExtension::isAttribute(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerPropertySheetExtension11isAttributeEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return self->isAttribute(index);
}

//  void QDesignerPropertySheetExtension::setAttribute(int index, bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtension12setAttributeEib(
    QDesignerPropertySheetExtension *self,
    int index,
    bool b) {
  self->setAttribute(index, b);
}

//  QVariant QDesignerPropertySheetExtension::property(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QDesignerPropertySheetExtension8propertyEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return new QVariant(self->property(index));
}

//  void QDesignerPropertySheetExtension::setProperty(int index, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtension11setPropertyEiRK8QVariant(
    QDesignerPropertySheetExtension *self,
    int index,
    const QVariant *value) {
  self->setProperty(index, *value);
}

//  bool QDesignerPropertySheetExtension::isChanged(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerPropertySheetExtension9isChangedEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return self->isChanged(index);
}

//  void QDesignerPropertySheetExtension::setChanged(int index, bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QDesignerPropertySheetExtension10setChangedEib(
    QDesignerPropertySheetExtension *self,
    int index,
    bool changed) {
  self->setChanged(index, changed);
}

//  bool QDesignerPropertySheetExtension::isEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QDesignerPropertySheetExtension9isEnabledEi(
    const QDesignerPropertySheetExtension *self,
    int index) {
  return self->isEnabled(index);
}

//  a Python function taken by a CuteQDesignerPropertySheetExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerPropertySheetExtension(
    QDesignerPropertySheetExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerPropertySheetExtension *>(self)->take(key, call);
}
