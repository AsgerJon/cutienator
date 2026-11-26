//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmljsloggingutils.h>
#include <memory>
#include <QtCore/QAnyStringView>
#include <unordered_map>

//  PassManagerPrivate *QQmlSA::PassManager::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA11PassManager6d_funcEv(
    QQmlSA::PassManager *self) {
  return self->d_func();
}

//  const PassManagerPrivate *QQmlSA::PassManager::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::PassManagerPrivate *ritual_ZNK6QQmlSA11PassManager6d_funcEv(
    const QQmlSA::PassManager *self) {
  return self->d_func();
}

//  bool
//      QQmlSA::PassManager::registerPropertyPass(std::shared_ptr<PropertyPas
//      s> pass, QAnyStringView moduleName, QAnyStringView typeName,
//      QAnyStringView propertyName, bool allowInheritance)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA11PassManager20registerPropertyPassESt10shared_ptrINS_12PropertyPassEE14QAnyStringViewS4_S4_b(
    QQmlSA::PassManager *self,
    const std::shared_ptr<QQmlSA::PropertyPass> *pass,
    const QString *moduleName,
    const QString *typeName,
    const QString *propertyName,
    bool allowInheritance) {
  return self->registerPropertyPass(
      *pass,
      QAnyStringView(*moduleName),
      QAnyStringView(*typeName),
      QAnyStringView(*propertyName),
      allowInheritance);
}

//  void QQmlSA::PassManager::analyze(const Element &root)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA11PassManager7analyzeERKNS_7ElementE(
    QQmlSA::PassManager *self,
    const QQmlSA::Element *root) {
  self->analyze(*root);
}

//  bool QQmlSA::PassManager::hasImportedModule(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA11PassManager17hasImportedModuleE14QAnyStringView(
    const QQmlSA::PassManager *self,
    const QString *name) {
  return self->hasImportedModule(QAnyStringView(*name));
}

//  bool QQmlSA::PassManager::isCategoryEnabled(LoggerWarningId category)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA11PassManager17isCategoryEnabledENS_15LoggerWarningIdE(
    const QQmlSA::PassManager *self,
    const QQmlSA::LoggerWarningId *category) {
  return self->isCategoryEnabled(*category);
}

//  std::unordered_map<quint32, Binding>
//      QQmlSA::PassManager::bindingsByLocation() const
extern "C" Q_DECL_EXPORT
std::unordered_map<quint32, QQmlSA::Binding> *ritual_ZNK6QQmlSA11PassManager18bindingsByLocationEv(
    const QQmlSA::PassManager *self) {
  return new std::unordered_map<quint32, QQmlSA::Binding>(
      self->bindingsByLocation());
}

//  QQmlSA::PassManager::PassManager()
extern "C" Q_DECL_EXPORT
QQmlSA::PassManager *ritual_ZN6QQmlSA11PassManagerC1Ev() {
  return new QQmlSA::PassManager();
}

//  QQmlSA::PassManager::~PassManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA11PassManagerD1Ev(QQmlSA::PassManager *self) {
  delete self;
}

//  a std::unordered_map<quint32, QQmlSA::Binding> a ritual of
//      QQmlSA::PassManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_PassManager__std_unordered_map_quint32_QQmlSA_Binding(
    std::unordered_map<quint32, QQmlSA::Binding> *self) {
  delete self;
}
