//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmltabledata.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmltabledata.h>
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlexecutablecontent.h>
#include <cstring>

//  A QScxmlTableData that Python can take functions over in. Every QScxmlTableData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQScxmlTableDataCall0)(const void *, QScxmlExecutableContent::StringId, int *);
typedef const QScxmlExecutableContent::EvaluatorInfo * (*CuteQScxmlTableDataCall1)(const void *, QScxmlExecutableContent::EvaluatorId, int *);
typedef const QScxmlExecutableContent::AssignmentInfo * (*CuteQScxmlTableDataCall2)(const void *, QScxmlExecutableContent::EvaluatorId, int *);
typedef const QScxmlExecutableContent::ForeachInfo * (*CuteQScxmlTableDataCall3)(const void *, QScxmlExecutableContent::EvaluatorId, int *);
typedef QScxmlExecutableContent::ContainerId (*CuteQScxmlTableDataCall4)(const void *, int *);
typedef QString * (*CuteQScxmlTableDataCall5)(const void *, int *);
typedef void * (*CuteQScxmlTableDataCall6)(const void *, int, int *);
class CuteQScxmlTableData : public QScxmlTableData {
public:
  using QScxmlTableData::QScxmlTableData;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QScxmlTableData6stringEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData13evaluatorInfoEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData14assignmentInfoEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData11foreachInfoEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData12initialSetupEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData4nameEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlTableData14serviceFactoryEi")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QString QScxmlTableData::string(QScxmlExecutableContent::StringId id)
  //      const
  QString string(QScxmlExecutableContent::StringId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlTableDataCall0 call = reinterpret_cast<CuteQScxmlTableDataCall0>(taken[0]);
      QString * given = call(this, id, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QScxmlExecutableContent::EvaluatorInfo
  //      QScxmlTableData::evaluatorInfo(QScxmlExecutableContent::Evaluator
  //      Id evaluatorId) const
  QScxmlExecutableContent::EvaluatorInfo evaluatorInfo(
      QScxmlExecutableContent::EvaluatorId evaluatorId) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlTableDataCall1 call = reinterpret_cast<CuteQScxmlTableDataCall1>(taken[1]);
      const QScxmlExecutableContent::EvaluatorInfo * given = call(this, evaluatorId, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QScxmlExecutableContent::AssignmentInfo
  //      QScxmlTableData::assignmentInfo(QScxmlExecutableContent::Evaluato
  //      rId assignmentId) const
  QScxmlExecutableContent::AssignmentInfo assignmentInfo(
      QScxmlExecutableContent::EvaluatorId assignmentId) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlTableDataCall2 call = reinterpret_cast<CuteQScxmlTableDataCall2>(taken[2]);
      const QScxmlExecutableContent::AssignmentInfo * given = call(this, assignmentId, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QScxmlExecutableContent::ForeachInfo
  //      QScxmlTableData::foreachInfo(QScxmlExecutableContent::EvaluatorId
  //      foreachId) const
  QScxmlExecutableContent::ForeachInfo foreachInfo(
      QScxmlExecutableContent::EvaluatorId foreachId) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlTableDataCall3 call = reinterpret_cast<CuteQScxmlTableDataCall3>(taken[3]);
      const QScxmlExecutableContent::ForeachInfo * given = call(this, foreachId, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QScxmlExecutableContent::ContainerId QScxmlTableData::initialSetup()
  //      const
  QScxmlExecutableContent::ContainerId initialSetup() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlTableDataCall4 call = reinterpret_cast<CuteQScxmlTableDataCall4>(taken[4]);
      QScxmlExecutableContent::ContainerId given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QScxmlTableData::name() const
  QString name() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQScxmlTableDataCall5 call = reinterpret_cast<CuteQScxmlTableDataCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QScxmlInvokableServiceFactory *QScxmlTableData::serviceFactory(int
  //      id) const
  QScxmlInvokableServiceFactory *serviceFactory(int id) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQScxmlTableDataCall6 call = reinterpret_cast<CuteQScxmlTableDataCall6>(taken[6]);
      void * given = call(this, id, &handled);
      if (handled) return static_cast<QScxmlInvokableServiceFactory *>(given);
    }
    return {};
  }
};

//  QScxmlTableData::~QScxmlTableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QScxmlTableDataD1Ev(QScxmlTableData *self) {
  delete self;
}

//  QString QScxmlTableData::string(QScxmlExecutableContent::StringId id)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QScxmlTableData6stringEi(
    const QScxmlTableData *self,
    QScxmlExecutableContent::StringId id) {
  return new QString(self->string(id));
}

//  QScxmlExecutableContent::EvaluatorInfo
//      QScxmlTableData::evaluatorInfo(QScxmlExecutableContent::EvaluatorId
//      evaluatorId) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::EvaluatorInfo *ritual_ZNK15QScxmlTableData13evaluatorInfoEi(
    const QScxmlTableData *self,
    QScxmlExecutableContent::EvaluatorId evaluatorId) {
  return new QScxmlExecutableContent::EvaluatorInfo(
      self->evaluatorInfo(
          evaluatorId));
}

//  QScxmlExecutableContent::AssignmentInfo
//      QScxmlTableData::assignmentInfo(QScxmlExecutableContent::EvaluatorId
//      assignmentId) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::AssignmentInfo *ritual_ZNK15QScxmlTableData14assignmentInfoEi(
    const QScxmlTableData *self,
    QScxmlExecutableContent::EvaluatorId assignmentId) {
  return new QScxmlExecutableContent::AssignmentInfo(
      self->assignmentInfo(
          assignmentId));
}

//  QScxmlExecutableContent::ForeachInfo
//      QScxmlTableData::foreachInfo(QScxmlExecutableContent::EvaluatorId
//      foreachId) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::ForeachInfo *ritual_ZNK15QScxmlTableData11foreachInfoEi(
    const QScxmlTableData *self,
    QScxmlExecutableContent::EvaluatorId foreachId) {
  return new QScxmlExecutableContent::ForeachInfo(
      self->foreachInfo(
          foreachId));
}

//  QScxmlExecutableContent::ContainerId QScxmlTableData::initialSetup()
//      const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::ContainerId ritual_ZNK15QScxmlTableData12initialSetupEv(
    const QScxmlTableData *self) {
  return self->initialSetup();
}

//  QString QScxmlTableData::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QScxmlTableData4nameEv(const QScxmlTableData *self) {
  return new QString(self->name());
}

//  QScxmlInvokableServiceFactory *QScxmlTableData::serviceFactory(int id)
//      const
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_ZNK15QScxmlTableData14serviceFactoryEi(
    const QScxmlTableData *self,
    int id) {
  return self->serviceFactory(id);
}

//  a Python function taken by a CuteQScxmlTableData, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlTableData(
    QScxmlTableData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlTableData *>(self)->take(key, call);
}
