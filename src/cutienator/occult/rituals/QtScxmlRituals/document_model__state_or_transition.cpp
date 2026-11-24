//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A DocumentModel::StateOrTransition that Python can take functions over in. Every DocumentModel::StateOrTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_StateOrTransitionCall0)(const void *, DocumentModel::NodeVisitor *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall1)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall2)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall3)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall4)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall5)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall6)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall7)(const void *, int *);
typedef void * (*CuteDocumentModel_StateOrTransitionCall8)(const void *, int *);
class CuteDocumentModel_StateOrTransition : public DocumentModel::StateOrTransition {
public:
  using DocumentModel::StateOrTransition::StateOrTransition;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6acceptEPNS_11NodeVisitorE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node4asIfEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6asSendEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asInvokeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asScriptEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asStateEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node12asTransitionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node14asHistoryStateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asScxmlEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void DocumentModel::Node::accept(NodeVisitor *visitor)
  void accept(DocumentModel::NodeVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall0 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
  }

  //  If *DocumentModel::Node::asIf()
  DocumentModel::If *asIf() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall1 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::If *>(given);
    }
    return DocumentModel::Node::asIf();
  }

  //  Send *DocumentModel::Node::asSend()
  DocumentModel::Send *asSend() override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall2 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Send *>(given);
    }
    return DocumentModel::Node::asSend();
  }

  //  Invoke *DocumentModel::Node::asInvoke()
  DocumentModel::Invoke *asInvoke() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall3 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Invoke *>(given);
    }
    return DocumentModel::Node::asInvoke();
  }

  //  Script *DocumentModel::Node::asScript()
  DocumentModel::Script *asScript() override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall4 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Script *>(given);
    }
    return DocumentModel::Node::asScript();
  }

  //  State *DocumentModel::Node::asState()
  DocumentModel::State *asState() override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall5 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::Node::asState();
  }

  //  Transition *DocumentModel::Node::asTransition()
  DocumentModel::Transition *asTransition() override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall6 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Transition *>(given);
    }
    return DocumentModel::Node::asTransition();
  }

  //  HistoryState *DocumentModel::Node::asHistoryState()
  DocumentModel::HistoryState *asHistoryState() override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall7 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::HistoryState *>(given);
    }
    return DocumentModel::Node::asHistoryState();
  }

  //  Scxml *DocumentModel::Node::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_StateOrTransitionCall8 call = reinterpret_cast<CuteDocumentModel_StateOrTransitionCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::Node::asScxml();
  }
};

//  a Python function taken by a CuteDocumentModel_StateOrTransition, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_StateOrTransition(
    DocumentModel::StateOrTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_StateOrTransition *>(self)->take(key, call);
}
