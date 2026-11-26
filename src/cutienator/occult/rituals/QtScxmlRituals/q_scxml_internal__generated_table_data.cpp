//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmltabledata_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 4. Kept as it is when the generator runs again.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmltabledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlexecutablecontent.h>
#include <cstring>

//  A QScxmlInternal::GeneratedTableData that Python can take functions over in. Every QScxmlInternal::GeneratedTableData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlInternal_GeneratedTableDataCall0)(const void *, int, int *);
class CuteQScxmlInternal_GeneratedTableData : public QScxmlInternal::GeneratedTableData {
public:
  using QScxmlInternal::GeneratedTableData::GeneratedTableData;
  CuteQScxmlInternal_GeneratedTableData(const QScxmlInternal::GeneratedTableData & other) : QScxmlInternal::GeneratedTableData(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QScxmlTableData14serviceFactoryEi")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QScxmlInvokableServiceFactory
  //      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
  QScxmlInvokableServiceFactory *serviceFactory(int id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlInternal_GeneratedTableDataCall0 call = reinterpret_cast<CuteQScxmlInternal_GeneratedTableDataCall0>(taken[0]);
      void * given = call(this, id, &handled);
      if (handled) return static_cast<QScxmlInvokableServiceFactory *>(given);
    }
    return QScxmlInternal::GeneratedTableData::serviceFactory(id);
  }
};

//  void
//      QScxmlInternal::GeneratedTableData::build(DocumentModel::ScxmlDocumen
//      t *doc, GeneratedTableData *table, MetaDataInfo *metaDataInfo,
//      DataModelInfo *dataModelInfo, CreateFactoryId func)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal18GeneratedTableData5buildEPN13DocumentModel13ScxmlDocumentEPS0_PNS0_12MetaDataInfoEPNS0_13DataModelInfoESt8functionIFiRKN23QScxmlExecutableContent10InvokeInfoERK5QListIiERKSE_INSA_13ParameterInfoEE14QSharedPointerIS2_EEE(
    DocumentModel::ScxmlDocument *doc,
    QScxmlInternal::GeneratedTableData *table,
    QScxmlInternal::GeneratedTableData::MetaDataInfo *metaDataInfo,
    QScxmlInternal::GeneratedTableData::DataModelInfo *dataModelInfo,
    const QScxmlInternal::GeneratedTableData::CreateFactoryId *func) {
  QScxmlInternal::GeneratedTableData::build(
      doc,
      table,
      metaDataInfo,
      dataModelInfo,
      *func);
}

//  QString QScxmlInternal::GeneratedTableData::toString(const int
//      *stateMachineTable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QScxmlInternal18GeneratedTableData8toStringEPKi(
    const int *stateMachineTable) {
  return new QString(
      QScxmlInternal::GeneratedTableData::toString(
          stateMachineTable));
}

//  QString QScxmlInternal::GeneratedTableData::string(QScxmlExecutableConten
//      t::StringId id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QScxmlInternal18GeneratedTableData6stringEi(
    const QScxmlInternal::GeneratedTableData *self,
    QScxmlExecutableContent::StringId id) {
  return new QString(self->string(id));
}

//  QScxmlExecutableContent::EvaluatorInfo QScxmlInternal::GeneratedTableData
//      ::evaluatorInfo(QScxmlExecutableContent::EvaluatorId evaluatorId)
//      const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::EvaluatorInfo *ritual_ZNK14QScxmlInternal18GeneratedTableData13evaluatorInfoEi(
    const QScxmlInternal::GeneratedTableData *self,
    QScxmlExecutableContent::EvaluatorId evaluatorId) {
  return new QScxmlExecutableContent::EvaluatorInfo(
      self->evaluatorInfo(
          evaluatorId));
}

//  QScxmlExecutableContent::AssignmentInfo QScxmlInternal::GeneratedTableDat
//      a::assignmentInfo(QScxmlExecutableContent::EvaluatorId assignmentId)
//      const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::AssignmentInfo *ritual_ZNK14QScxmlInternal18GeneratedTableData14assignmentInfoEi(
    const QScxmlInternal::GeneratedTableData *self,
    QScxmlExecutableContent::EvaluatorId assignmentId) {
  return new QScxmlExecutableContent::AssignmentInfo(
      self->assignmentInfo(
          assignmentId));
}

//  QScxmlExecutableContent::ForeachInfo QScxmlInternal::GeneratedTableData::
//      foreachInfo(QScxmlExecutableContent::EvaluatorId foreachId) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::ForeachInfo *ritual_ZNK14QScxmlInternal18GeneratedTableData11foreachInfoEi(
    const QScxmlInternal::GeneratedTableData *self,
    QScxmlExecutableContent::EvaluatorId foreachId) {
  return new QScxmlExecutableContent::ForeachInfo(
      self->foreachInfo(
          foreachId));
}

//  QScxmlExecutableContent::ContainerId
//      QScxmlInternal::GeneratedTableData::initialSetup() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::ContainerId ritual_ZNK14QScxmlInternal18GeneratedTableData12initialSetupEv(
    const QScxmlInternal::GeneratedTableData *self) {
  return self->initialSetup();
}

//  QString QScxmlInternal::GeneratedTableData::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QScxmlInternal18GeneratedTableData4nameEv(
    const QScxmlInternal::GeneratedTableData *self) {
  return new QString(self->name());
}

//  const qint32 *QScxmlInternal::GeneratedTableData::stateMachineTable()
//      const
extern "C" Q_DECL_EXPORT
const qint32 *ritual_ZNK14QScxmlInternal18GeneratedTableData17stateMachineTableEv(
    const QScxmlInternal::GeneratedTableData *self) {
  return self->stateMachineTable();
}

//  QScxmlInvokableServiceFactory
//      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_ZNK14QScxmlInternal18GeneratedTableData14serviceFactoryEi(
    const QScxmlInternal::GeneratedTableData *self,
    int id) {
  return self->serviceFactory(id);
}

//  QScxmlInternal::GeneratedTableData::~GeneratedTableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal18GeneratedTableDataD1Ev(
    QScxmlInternal::GeneratedTableData *self) {
  delete self;
}

//  a Python function taken by a CuteQScxmlInternal_GeneratedTableData, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInternal_GeneratedTableData(
    QScxmlInternal::GeneratedTableData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInternal_GeneratedTableData *>(self)->take(key, call);
}

//  QScxmlInvokableServiceFactory
//      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_own_ZNK14QScxmlInternal18GeneratedTableData14serviceFactoryEi(
    const QScxmlInternal::GeneratedTableData *self,
    int id) {
  return self->QScxmlInternal::GeneratedTableData::serviceFactory(id);
}

//  QScxmlExecutableContent::InstructionId
//      *QScxmlInternal::GeneratedTableData::instructions() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::InstructionId *ritual_ZNK14QScxmlInternal18GeneratedTableData12instructionsEv(
    const QScxmlInternal::GeneratedTableData *self) {
  return self->instructions();
}

//  QScxmlExecutableContent::InstructionId
//      *QScxmlInternal::GeneratedTableData::instructions() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::InstructionId *ritual_own_ZNK14QScxmlInternal18GeneratedTableData12instructionsEv(
    const QScxmlInternal::GeneratedTableData *self) {
  return self->QScxmlInternal::GeneratedTableData::instructions();
}

//  QScxmlExecutableContent::StringId
//      *QScxmlInternal::GeneratedTableData::dataNames(int *count) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StringId *ritual_ZNK14QScxmlInternal18GeneratedTableData9dataNamesEPi(
    const QScxmlInternal::GeneratedTableData *self,
    int *count) {
  return self->dataNames(count);
}

//  QScxmlExecutableContent::StringId
//      *QScxmlInternal::GeneratedTableData::dataNames(int *count) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StringId *ritual_own_ZNK14QScxmlInternal18GeneratedTableData9dataNamesEPi(
    const QScxmlInternal::GeneratedTableData *self,
    int *count) {
  return self->QScxmlInternal::GeneratedTableData::dataNames(count);
}
