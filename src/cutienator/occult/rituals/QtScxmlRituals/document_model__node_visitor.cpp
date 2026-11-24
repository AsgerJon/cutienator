//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A DocumentModel::NodeVisitor that Python can take functions over in. Every DocumentModel::NodeVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_NodeVisitorCall0)(const void *, DocumentModel::DataElement *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall1)(const void *, DocumentModel::Param *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall2)(const void *, DocumentModel::DoneData *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall3)(const void *, DocumentModel::DoneData *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall4)(const void *, DocumentModel::Send *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall5)(const void *, DocumentModel::Send *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall6)(const void *, DocumentModel::Invoke *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall7)(const void *, DocumentModel::Invoke *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall8)(const void *, DocumentModel::Raise *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall9)(const void *, DocumentModel::Log *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall10)(const void *, DocumentModel::Script *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall11)(const void *, DocumentModel::Assign *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall12)(const void *, DocumentModel::If *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall13)(const void *, DocumentModel::If *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall14)(const void *, DocumentModel::Foreach *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall15)(const void *, DocumentModel::Foreach *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall16)(const void *, DocumentModel::Cancel *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall17)(const void *, DocumentModel::State *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall18)(const void *, DocumentModel::State *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall19)(const void *, DocumentModel::Transition *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall20)(const void *, DocumentModel::Transition *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall21)(const void *, DocumentModel::HistoryState *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall22)(const void *, DocumentModel::HistoryState *, int *);
typedef bool (*CuteDocumentModel_NodeVisitorCall23)(const void *, DocumentModel::Scxml *, int *);
typedef void (*CuteDocumentModel_NodeVisitorCall24)(const void *, DocumentModel::Scxml *, int *);
class CuteDocumentModel_NodeVisitor : public DocumentModel::NodeVisitor {
public:
  using DocumentModel::NodeVisitor::NodeVisitor;
  CuteDocumentModel_NodeVisitor(const DocumentModel::NodeVisitor &other) : DocumentModel::NodeVisitor(other) {}
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElementE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_10TransitionE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10TransitionE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistoryStateE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12HistoryStateE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE")) {
      taken[24] = call;
      return true;
    }
    return false;
  }

  //  void DocumentModel::NodeVisitor::visit(DataElement *a0)
  void visit(DocumentModel::DataElement *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall0 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Param *a0)
  void visit(DocumentModel::Param *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall1 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(DoneData *a0)
  bool visit(DocumentModel::DoneData *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall2 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(DoneData *a0)
  void endVisit(DocumentModel::DoneData *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall3 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(Send *a0)
  bool visit(DocumentModel::Send *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall4 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(Send *a0)
  void endVisit(DocumentModel::Send *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall5 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(Invoke *a0)
  bool visit(DocumentModel::Invoke *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall6 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(Invoke *a0)
  void endVisit(DocumentModel::Invoke *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall7 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Raise *a0)
  void visit(DocumentModel::Raise *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall8 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Log *a0)
  void visit(DocumentModel::Log *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall9 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Script *a0)
  void visit(DocumentModel::Script *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall10 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Assign *a0)
  void visit(DocumentModel::Assign *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall11 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(If *a0)
  bool visit(DocumentModel::If *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall12 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(If *a0)
  void endVisit(DocumentModel::If *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall13 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(Foreach *a0)
  bool visit(DocumentModel::Foreach *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall14 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(Foreach *a0)
  void endVisit(DocumentModel::Foreach *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall15 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  void DocumentModel::NodeVisitor::visit(Cancel *a0)
  void visit(DocumentModel::Cancel *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall16 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::visit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(State *a0)
  bool visit(DocumentModel::State *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall17 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(State *a0)
  void endVisit(DocumentModel::State *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall18 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(Transition *a0)
  bool visit(DocumentModel::Transition *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall19 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall19>(taken[19]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(Transition *a0)
  void endVisit(DocumentModel::Transition *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall20 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(HistoryState *a0)
  bool visit(DocumentModel::HistoryState *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall21 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall21>(taken[21]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(HistoryState *a0)
  void endVisit(DocumentModel::HistoryState *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall22 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }

  //  bool DocumentModel::NodeVisitor::visit(Scxml *a0)
  bool visit(DocumentModel::Scxml *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall23 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall23>(taken[23]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return DocumentModel::NodeVisitor::visit(a0);
  }

  //  void DocumentModel::NodeVisitor::endVisit(Scxml *a0)
  void endVisit(DocumentModel::Scxml *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteDocumentModel_NodeVisitorCall24 call = reinterpret_cast<CuteDocumentModel_NodeVisitorCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    DocumentModel::NodeVisitor::endVisit(a0);
  }
};

//  DocumentModel::NodeVisitor::~NodeVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitorD1Ev(
    DocumentModel::NodeVisitor *self) {
  delete self;
}

//  void DocumentModel::NodeVisitor::visit(DataElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElementE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DataElement *a0) {
  self->visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Param *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Param *a0) {
  self->visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(DoneData *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DoneData *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(DoneData *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneDataE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DoneData *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Send *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Send *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Send *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Send *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Invoke *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Invoke *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Invoke *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Invoke *a0) {
  self->endVisit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Raise *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Raise *a0) {
  self->visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Log *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Log *a0) {
  self->visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Script *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Script *a0) {
  self->visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Assign *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Assign *a0) {
  self->visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(If *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::If *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(If *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::If *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Foreach *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Foreach *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Foreach *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Foreach *a0) {
  self->endVisit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Cancel *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Cancel *a0) {
  self->visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(State *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::State *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(State *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::State *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Transition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_10TransitionE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Transition *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Transition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10TransitionE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Transition *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(HistoryState *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistoryStateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::HistoryState *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(HistoryState *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12HistoryStateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::HistoryState *a0) {
  self->endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Scxml *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Scxml *a0) {
  return self->visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Scxml *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Scxml *a0) {
  self->endVisit(a0);
}

//  a Python function taken by a CuteDocumentModel_NodeVisitor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_NodeVisitor(
    DocumentModel::NodeVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_NodeVisitor *>(self)->take(key, call);
}

//  void DocumentModel::NodeVisitor::visit(DataElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElementE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DataElement *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Param *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Param *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(DoneData *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DoneData *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(DoneData *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneDataE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::DoneData *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Send *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Send *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Send *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Send *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Invoke *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Invoke *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Invoke *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Invoke *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Raise *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Raise *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Log *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Log *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Script *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Script *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Assign *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Assign *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(If *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::If *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(If *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::If *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Foreach *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Foreach *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Foreach *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Foreach *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  void DocumentModel::NodeVisitor::visit(Cancel *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Cancel *a0) {
  self->DocumentModel::NodeVisitor::visit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(State *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::State *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(State *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::State *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Transition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_10TransitionE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Transition *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Transition *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10TransitionE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Transition *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(HistoryState *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistoryStateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::HistoryState *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(HistoryState *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12HistoryStateE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::HistoryState *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}

//  bool DocumentModel::NodeVisitor::visit(Scxml *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Scxml *a0) {
  return self->DocumentModel::NodeVisitor::visit(a0);
}

//  void DocumentModel::NodeVisitor::endVisit(Scxml *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE(
    DocumentModel::NodeVisitor *self,
    DocumentModel::Scxml *a0) {
  self->DocumentModel::NodeVisitor::endVisit(a0);
}
