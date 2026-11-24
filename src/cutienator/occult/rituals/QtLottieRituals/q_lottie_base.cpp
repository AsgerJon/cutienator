//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiebase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QLottieBase that Python can take functions over in. Every QLottieBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieBaseCall0)(const void *, int *);
typedef bool (*CuteQLottieBaseCall1)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieBaseCall2)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieBaseCall3)(const void *, int, int *);
typedef void * (*CuteQLottieBaseCall4)(const void *, const QString *, int *);
typedef void (*CuteQLottieBaseCall5)(const void *, int, int *);
typedef const QSize * (*CuteQLottieBaseCall6)(const void *, int *);
class CuteQLottieBase : public QLottieBase {
public:
  using QLottieBase::QLottieBase;
  CuteQLottieBase(const QLottieBase &other) : QLottieBase(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieBase::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieBaseCall0 call = reinterpret_cast<CuteQLottieBaseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::clone();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieBaseCall1 call = reinterpret_cast<CuteQLottieBaseCall1>(taken[1]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieBaseCall2 call = reinterpret_cast<CuteQLottieBaseCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieBaseCall3 call = reinterpret_cast<CuteQLottieBaseCall3>(taken[3]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieBaseCall4 call = reinterpret_cast<CuteQLottieBaseCall4>(taken[4]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  void QLottieBase::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieBaseCall5 call = reinterpret_cast<CuteQLottieBaseCall5>(taken[5]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieBase::updateProperties(frame);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieBaseCall6 call = reinterpret_cast<CuteQLottieBaseCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieBase::QLottieBase()
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZN11QLottieBaseC1Ev() {
  return new CuteQLottieBase();
}

//  QLottieBase::QLottieBase(const QLottieBase &other)
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZN11QLottieBaseC1ERKS_(const QLottieBase *other) {
  return new CuteQLottieBase(*other);
}

//  QLottieBase::~QLottieBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBaseD1Ev(QLottieBase *self) {
  delete self;
}

//  QLottieBase *QLottieBase::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieBase5cloneEv(const QLottieBase *self) {
  return self->clone();
}

//  bool QLottieBase::setProperty(QLottieLiteral::PropertyType propertyType,
//      QVariant value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant(
    QLottieBase *self,
    QLottieLiteral::PropertyType propertyType,
    const QVariant *value) {
  return self->setProperty(propertyType, *value);
}

//  QString QLottieBase::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLottieBase4nameEv(const QLottieBase *self) {
  return new QString(self->name());
}

//  void QLottieBase::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase7setNameERK7QString(
    QLottieBase *self,
    const QString *name) {
  self->setName(*name);
}

//  int QLottieBase::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLottieBase4typeEv(const QLottieBase *self) {
  return self->type();
}

//  void QLottieBase::setType(int type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase7setTypeEi(QLottieBase *self, int type) {
  self->setType(type);
}

//  bool QLottieBase::isShapeElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieBase14isShapeElementEv(const QLottieBase *self) {
  return self->isShapeElement();
}

//  bool QLottieBase::isPathElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieBase13isPathElementEv(const QLottieBase *self) {
  return self->isPathElement();
}

//  int QLottieBase::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QLottieBase5parseERK11QJsonObject(
    QLottieBase *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  const QJsonObject &QLottieBase::definition() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK11QLottieBase10definitionEv(const QLottieBase *self) {
  return new QJsonObject(self->definition());
}

//  bool QLottieBase::active(int frame) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieBase6activeEi(const QLottieBase *self, int frame) {
  return self->active(frame);
}

//  bool QLottieBase::hidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieBase6hiddenEv(const QLottieBase *self) {
  return self->hidden();
}

//  QLottieBase *QLottieBase::parent() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieBase6parentEv(const QLottieBase *self) {
  return self->parent();
}

//  void QLottieBase::setParent(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase9setParentEPS_(
    QLottieBase *self,
    QLottieBase *parent) {
  self->setParent(parent);
}

//  const QList<QLottieBase *> &QLottieBase::children() const
extern "C" Q_DECL_EXPORT
QList<QLottieBase *> *ritual_ZNK11QLottieBase8childrenEv(
    const QLottieBase *self) {
  return new QList<QLottieBase *>(self->children());
}

//  void QLottieBase::prependChild(QLottieBase *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase12prependChildEPS_(
    QLottieBase *self,
    QLottieBase *child) {
  self->prependChild(child);
}

//  void QLottieBase::insertChildBeforeLast(QLottieBase *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase21insertChildBeforeLastEPS_(
    QLottieBase *self,
    QLottieBase *child) {
  self->insertChildBeforeLast(child);
}

//  void QLottieBase::appendChild(QLottieBase *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase11appendChildEPS_(
    QLottieBase *self,
    QLottieBase *child) {
  self->appendChild(child);
}

//  QLottieBase *QLottieBase::findChild(const QString &childName)
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZN11QLottieBase9findChildERK7QString(
    QLottieBase *self,
    const QString *childName) {
  return self->findChild(*childName);
}

//  void QLottieBase::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase16updatePropertiesEi(
    QLottieBase *self,
    int frame) {
  self->updateProperties(frame);
}

//  QSize QLottieBase::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLottieBase9layerSizeEv(const QLottieBase *self) {
  return new QSize(self->layerSize());
}

//  bool QLottieBase::isStructureDumping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieBase18isStructureDumpingEv(const QLottieBase *self) {
  return self->isStructureDumping();
}

//  void QLottieBase::resolveTopRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieBase14resolveTopRootEv(QLottieBase *self) {
  self->resolveTopRoot();
}

//  QLottieBase *QLottieBase::topRoot() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieBase7topRootEv(const QLottieBase *self) {
  return self->topRoot();
}

//  const QJsonObject QLottieBase::resolveExpression(const QJsonObject
//      &definition)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN11QLottieBase17resolveExpressionERK11QJsonObject(
    QLottieBase *self,
    const QJsonObject *definition) {
  return new QJsonObject(self->resolveExpression(*definition));
}

//  a Python function taken by a CuteQLottieBase, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieBase(
    QLottieBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieBase *>(self)->take(key, call);
}

//  QLottieBase *QLottieBase::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK11QLottieBase5cloneEv(const QLottieBase *self) {
  return self->QLottieBase::clone();
}

//  bool QLottieBase::setProperty(QLottieLiteral::PropertyType propertyType,
//      QVariant value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant(
    QLottieBase *self,
    QLottieLiteral::PropertyType propertyType,
    const QVariant *value) {
  return self->QLottieBase::setProperty(propertyType, *value);
}

//  int QLottieBase::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN11QLottieBase5parseERK11QJsonObject(
    QLottieBase *self,
    const QJsonObject *definition) {
  return self->QLottieBase::parse(*definition);
}

//  bool QLottieBase::active(int frame) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QLottieBase6activeEi(
    const QLottieBase *self,
    int frame) {
  return self->QLottieBase::active(frame);
}

//  QLottieBase *QLottieBase::findChild(const QString &childName)
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZN11QLottieBase9findChildERK7QString(
    QLottieBase *self,
    const QString *childName) {
  return self->QLottieBase::findChild(*childName);
}

//  void QLottieBase::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLottieBase16updatePropertiesEi(
    QLottieBase *self,
    int frame) {
  self->QLottieBase::updateProperties(frame);
}

//  QSize QLottieBase::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QLottieBase9layerSizeEv(const QLottieBase *self) {
  return new QSize(self->QLottieBase::layerSize());
}

//  QList<QLottieBase *>::QList()
extern "C" Q_DECL_EXPORT
QList<QLottieBase *> *ritual_list_make_QLottieBase_ptr() {
  return new QList<QLottieBase *>();
}

//  void QList<QLottieBase *>::append(const QLottieBase * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLottieBase_ptr(
    QList<QLottieBase *> *self,
    QLottieBase *element) {
  self->append(element);
}

//  qsizetype QList<QLottieBase *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLottieBase_ptr(
    const QList<QLottieBase *> *self) {
  return self->size();
}

//  const QLottieBase * &QList<QLottieBase *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_list_at_QLottieBase_ptr(
    const QList<QLottieBase *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QLottieBase *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLottieBase_ptr(QList<QLottieBase *> *self) {
  delete self;
}
