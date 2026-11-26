//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractpromotioninterface.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractpromotioninterface.h>
#include <QtCore/qstring.h>
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtDesigner/QDesignerPromotionInterface>
#include <QtCore/QSet>
#include <QtCore/QString>

//  A QDesignerPromotionInterface that Python can take functions over in. Every QDesignerPromotionInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDesignerPromotionInterfaceCall0)(const void *, const QString *, const QString *, const QString *, QString *, int *);
typedef bool (*CuteQDesignerPromotionInterfaceCall1)(const void *, const QString *, QString *, int *);
typedef bool (*CuteQDesignerPromotionInterfaceCall2)(const void *, const QString *, const QString *, QString *, int *);
typedef bool (*CuteQDesignerPromotionInterfaceCall3)(const void *, const QString *, const QString *, QString *, int *);
class CuteQDesignerPromotionInterface : public QDesignerPromotionInterface {
public:
  using QDesignerPromotionInterface::QDesignerPromotionInterface;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QDesignerPromotionInterface16addPromotedClassERK7QStringS2_S2_PS0_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerPromotionInterface19removePromotedClassERK7QStringPS0_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerPromotionInterface23changePromotedClassNameERK7QStringS2_PS0_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerPromotionInterface27setPromotedClassIncludeFileERK7QStringS2_PS0_")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QDesignerPromotionInterface::addPromotedClass(const QString
  //      &baseClass, const QString &className, const QString &includeFile,
  //      QString *errorMessage)
  bool addPromotedClass(
      const QString &baseClass,
      const QString &className,
      const QString &includeFile,
      QString *errorMessage) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerPromotionInterfaceCall0 call = reinterpret_cast<CuteQDesignerPromotionInterfaceCall0>(taken[0]);
      bool given = call(this, &baseClass, &className, &includeFile, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerPromotionInterface::removePromotedClass(const QString
  //      &className, QString *errorMessage)
  bool removePromotedClass(
      const QString &className,
      QString *errorMessage) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerPromotionInterfaceCall1 call = reinterpret_cast<CuteQDesignerPromotionInterfaceCall1>(taken[1]);
      bool given = call(this, &className, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerPromotionInterface::changePromotedClassName(const
  //      QString &oldClassName, const QString &newClassName, QString
  //      *errorMessage)
  bool changePromotedClassName(
      const QString &oldClassName,
      const QString &newClassName,
      QString *errorMessage) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerPromotionInterfaceCall2 call = reinterpret_cast<CuteQDesignerPromotionInterfaceCall2>(taken[2]);
      bool given = call(this, &oldClassName, &newClassName, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerPromotionInterface::setPromotedClassIncludeFile(const
  //      QString &className, const QString &includeFile, QString
  //      *errorMessage)
  bool setPromotedClassIncludeFile(
      const QString &className,
      const QString &includeFile,
      QString *errorMessage) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerPromotionInterfaceCall3 call = reinterpret_cast<CuteQDesignerPromotionInterfaceCall3>(taken[3]);
      bool given = call(this, &className, &includeFile, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDesignerPromotionInterface::~QDesignerPromotionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerPromotionInterfaceD1Ev(
    QDesignerPromotionInterface *self) {
  delete self;
}

//  PromotedClasses QDesignerPromotionInterface::promotedClasses() const
extern "C" Q_DECL_EXPORT
QDesignerPromotionInterface::PromotedClasses *ritual_ZNK27QDesignerPromotionInterface15promotedClassesEv(
    const QDesignerPromotionInterface *self) {
  return new QDesignerPromotionInterface::PromotedClasses(
      self->promotedClasses());
}

//  QSet<QString> QDesignerPromotionInterface::referencedPromotedClassNames()
//      const
extern "C" Q_DECL_EXPORT
QSet<QString> *ritual_ZNK27QDesignerPromotionInterface28referencedPromotedClassNamesEv(
    const QDesignerPromotionInterface *self) {
  return new QSet<QString>(self->referencedPromotedClassNames());
}

//  bool QDesignerPromotionInterface::addPromotedClass(const QString
//      &baseClass, const QString &className, const QString &includeFile,
//      QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerPromotionInterface16addPromotedClassERK7QStringS2_S2_PS0_(
    QDesignerPromotionInterface *self,
    const QString *baseClass,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->addPromotedClass(
      *baseClass,
      *className,
      *includeFile,
      errorMessage);
}

//  bool QDesignerPromotionInterface::removePromotedClass(const QString
//      &className, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerPromotionInterface19removePromotedClassERK7QStringPS0_(
    QDesignerPromotionInterface *self,
    const QString *className,
    QString *errorMessage) {
  return self->removePromotedClass(*className, errorMessage);
}

//  bool QDesignerPromotionInterface::changePromotedClassName(const QString
//      &oldClassName, const QString &newClassName, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerPromotionInterface23changePromotedClassNameERK7QStringS2_PS0_(
    QDesignerPromotionInterface *self,
    const QString *oldClassName,
    const QString *newClassName,
    QString *errorMessage) {
  return self->changePromotedClassName(
      *oldClassName,
      *newClassName,
      errorMessage);
}

//  bool QDesignerPromotionInterface::setPromotedClassIncludeFile(const
//      QString &className, const QString &includeFile, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerPromotionInterface27setPromotedClassIncludeFileERK7QStringS2_PS0_(
    QDesignerPromotionInterface *self,
    const QString *className,
    const QString *includeFile,
    QString *errorMessage) {
  return self->setPromotedClassIncludeFile(
      *className,
      *includeFile,
      errorMessage);
}

//  QList<QDesignerWidgetDataBaseItemInterface *>
//      QDesignerPromotionInterface::promotionBaseClasses() const
extern "C" Q_DECL_EXPORT
QList<QDesignerWidgetDataBaseItemInterface *> *ritual_ZNK27QDesignerPromotionInterface20promotionBaseClassesEv(
    const QDesignerPromotionInterface *self) {
  return new QList<QDesignerWidgetDataBaseItemInterface *>(
      self->promotionBaseClasses());
}

//  a Python function taken by a CuteQDesignerPromotionInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerPromotionInterface(
    QDesignerPromotionInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerPromotionInterface *>(self)->take(key, call);
}

//  a QDesignerPromotionInterface::PromotedClasses a ritual of
//      QDesignerPromotionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDesignerPromotionInterface__QDesignerPromotionInterface_PromotedClasses(
    QDesignerPromotionInterface::PromotedClasses *self) {
  delete self;
}

//  a QSet<QString> a ritual of QDesignerPromotionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDesignerPromotionInterface__QSet_QString(
    QSet<QString> *self) {
  delete self;
}
