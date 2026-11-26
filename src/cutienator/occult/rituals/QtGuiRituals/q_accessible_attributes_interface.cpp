//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>
#include <cstring>
#include <QtCore/QList>
#include <QtGui/QAccessible>

//  A QAccessibleAttributesInterface that Python can take functions over in. Every QAccessibleAttributesInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleAttributesInterfaceCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleAttributesInterface : public QAccessibleAttributesInterface {
public:
  using QAccessibleAttributesInterface::QAccessibleAttributesInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QVariant
  //      QAccessibleAttributesInterface::attributeValue(QAccessible::Attri
  //      bute key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleAttributesInterfaceCall0 call = reinterpret_cast<CuteQAccessibleAttributesInterfaceCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleAttributesInterface::~QAccessibleAttributesInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QAccessibleAttributesInterfaceD1Ev(
    QAccessibleAttributesInterface *self) {
  delete self;
}

//  QList<QAccessible::Attribute>
//      QAccessibleAttributesInterface::attributeKeys() const
extern "C" Q_DECL_EXPORT
QList<QAccessible::Attribute> *ritual_ZNK30QAccessibleAttributesInterface13attributeKeysEv(
    const QAccessibleAttributesInterface *self) {
  return new QList<QAccessible::Attribute>(self->attributeKeys());
}

//  QVariant
//      QAccessibleAttributesInterface::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleAttributesInterface *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  a Python function taken by a CuteQAccessibleAttributesInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleAttributesInterface(
    QAccessibleAttributesInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleAttributesInterface *>(self)->take(key, call);
}

//  a QList<QAccessible::Attribute> a ritual of
//      QAccessibleAttributesInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleAttributesInterface__QList_QAccessible_Attribute(
    QList<QAccessible::Attribute> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
