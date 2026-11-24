//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/dynamicpropertysheet.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/dynamicpropertysheet.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QDesignerDynamicPropertySheetExtension that Python can take functions over in. Every QDesignerDynamicPropertySheetExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDesignerDynamicPropertySheetExtensionCall0)(const void *, int *);
typedef int (*CuteQDesignerDynamicPropertySheetExtensionCall1)(const void *, const QString *, const QVariant *, int *);
typedef bool (*CuteQDesignerDynamicPropertySheetExtensionCall2)(const void *, int, int *);
typedef bool (*CuteQDesignerDynamicPropertySheetExtensionCall3)(const void *, int, int *);
typedef bool (*CuteQDesignerDynamicPropertySheetExtensionCall4)(const void *, const QString *, int *);
class CuteQDesignerDynamicPropertySheetExtension : public QDesignerDynamicPropertySheetExtension {
public:
  using QDesignerDynamicPropertySheetExtension::QDesignerDynamicPropertySheetExtension;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension24dynamicPropertiesAllowedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension18addDynamicPropertyERK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPropertyEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicPropertyEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicPropertyERK7QString")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  bool
  //      QDesignerDynamicPropertySheetExtension::dynamicPropertiesAllowed(
  //      ) const
  bool dynamicPropertiesAllowed() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerDynamicPropertySheetExtensionCall0 call = reinterpret_cast<CuteQDesignerDynamicPropertySheetExtensionCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerDynamicPropertySheetExtension::addDynamicProperty(const
  //      QString &propertyName, const QVariant &value)
  int addDynamicProperty(
      const QString &propertyName,
      const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerDynamicPropertySheetExtensionCall1 call = reinterpret_cast<CuteQDesignerDynamicPropertySheetExtensionCall1>(taken[1]);
      int given = call(this, &propertyName, &value, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool
  //      QDesignerDynamicPropertySheetExtension::removeDynamicProperty(int
  //      index)
  bool removeDynamicProperty(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerDynamicPropertySheetExtensionCall2 call = reinterpret_cast<CuteQDesignerDynamicPropertySheetExtensionCall2>(taken[2]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerDynamicPropertySheetExtension::isDynamicProperty(int
  //      index) const
  bool isDynamicProperty(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerDynamicPropertySheetExtensionCall3 call = reinterpret_cast<CuteQDesignerDynamicPropertySheetExtensionCall3>(taken[3]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool
  //      QDesignerDynamicPropertySheetExtension::canAddDynamicProperty(con
  //      st QString &propertyName) const
  bool canAddDynamicProperty(const QString &propertyName) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerDynamicPropertySheetExtensionCall4 call = reinterpret_cast<CuteQDesignerDynamicPropertySheetExtensionCall4>(taken[4]);
      bool given = call(this, &propertyName, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDesignerDynamicPropertySheetExtension::~QDesignerDynamicPropertySheetExt
//      ension()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QDesignerDynamicPropertySheetExtensionD1Ev(
    QDesignerDynamicPropertySheetExtension *self) {
  delete self;
}

//  bool QDesignerDynamicPropertySheetExtension::dynamicPropertiesAllowed()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QDesignerDynamicPropertySheetExtension24dynamicPropertiesAllowedEv(
    const QDesignerDynamicPropertySheetExtension *self) {
  return self->dynamicPropertiesAllowed();
}

//  int QDesignerDynamicPropertySheetExtension::addDynamicProperty(const
//      QString &propertyName, const QVariant &value)
extern "C" Q_DECL_EXPORT
int ritual_ZN38QDesignerDynamicPropertySheetExtension18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerDynamicPropertySheetExtension *self,
    const QString *propertyName,
    const QVariant *value) {
  return self->addDynamicProperty(*propertyName, *value);
}

//  bool QDesignerDynamicPropertySheetExtension::removeDynamicProperty(int
//      index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPropertyEi(
    QDesignerDynamicPropertySheetExtension *self,
    int index) {
  return self->removeDynamicProperty(index);
}

//  bool QDesignerDynamicPropertySheetExtension::isDynamicProperty(int index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicPropertyEi(
    const QDesignerDynamicPropertySheetExtension *self,
    int index) {
  return self->isDynamicProperty(index);
}

//  bool QDesignerDynamicPropertySheetExtension::canAddDynamicProperty(const
//      QString &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicPropertyERK7QString(
    const QDesignerDynamicPropertySheetExtension *self,
    const QString *propertyName) {
  return self->canAddDynamicProperty(*propertyName);
}

//  a Python function taken by a CuteQDesignerDynamicPropertySheetExtension,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerDynamicPropertySheetExtension(
    QDesignerDynamicPropertySheetExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerDynamicPropertySheetExtension *>(self)->take(key, call);
}
