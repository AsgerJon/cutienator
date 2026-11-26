//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlcompiler_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qfile.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#ifndef BUILD_QSCXMLC
#include <QtScxml/private/qscxmlinvokableservice_p.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/qscxmlstatemachine.h>
#include <QtScxml/private/qscxmltabledata_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1144, as _ZN13DocumentModel4NodeD2Ev
inline DocumentModel::Node::~Node()
{
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1234, as _ZN13DocumentModel5State6acceptEPNS_11NodeVisitorE
inline void DocumentModel::State::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        visitor->visit(dataElements);
        visitor->visit(children);
        visitor->visit(onEntry);
        visitor->visit(onExit);
        if (doneData)
            doneData->accept(visitor);
        for (Invoke *invoke : std::as_const(invokes))
            invoke->accept(visitor);
    }
    visitor->endVisit(this);
}
//  -----------------------------------------------------------------------

//  A DocumentModel::State that Python can take functions over in. Every DocumentModel::State
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_StateCall0)(const void *, DocumentModel::StateOrTransition *, int *);
typedef void * (*CuteDocumentModel_StateCall1)(const void *, int *);
typedef void (*CuteDocumentModel_StateCall2)(const void *, DocumentModel::NodeVisitor *, int *);
typedef void * (*CuteDocumentModel_StateCall3)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall4)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall5)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall6)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall7)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall8)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall9)(const void *, int *);
typedef void * (*CuteDocumentModel_StateCall10)(const void *, int *);
class CuteDocumentModel_State : public DocumentModel::State {
public:
  using DocumentModel::State::State;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asStateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6acceptEPNS_11NodeVisitorE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node15asAbstractStateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asScxmlEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node4asIfEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6asSendEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asInvokeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asScriptEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node12asTransitionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node14asHistoryStateEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void DocumentModel::State::add(StateOrTransition *s)
  void add(DocumentModel::StateOrTransition *s) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_StateCall0 call = reinterpret_cast<CuteDocumentModel_StateCall0>(taken[0]);
      call(this, s, &handled);
      if (handled) return;
    }
    DocumentModel::State::add(s);
  }

  //  State *DocumentModel::State::asState()
  DocumentModel::State *asState() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_StateCall1 call = reinterpret_cast<CuteDocumentModel_StateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::State::asState();
  }

  //  void DocumentModel::State::accept(NodeVisitor *visitor)
  void accept(DocumentModel::NodeVisitor *visitor) override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_StateCall2 call = reinterpret_cast<CuteDocumentModel_StateCall2>(taken[2]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    DocumentModel::State::accept(visitor);
  }

  //  AbstractState *DocumentModel::AbstractState::asAbstractState()
  DocumentModel::AbstractState *asAbstractState() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_StateCall3 call = reinterpret_cast<CuteDocumentModel_StateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::AbstractState *>(given);
    }
    return DocumentModel::AbstractState::asAbstractState();
  }

  //  Scxml *DocumentModel::StateContainer::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_StateCall4 call = reinterpret_cast<CuteDocumentModel_StateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::StateContainer::asScxml();
  }

  //  If *DocumentModel::Node::asIf()
  DocumentModel::If *asIf() override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_StateCall5 call = reinterpret_cast<CuteDocumentModel_StateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::If *>(given);
    }
    return DocumentModel::Node::asIf();
  }

  //  Send *DocumentModel::Node::asSend()
  DocumentModel::Send *asSend() override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_StateCall6 call = reinterpret_cast<CuteDocumentModel_StateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Send *>(given);
    }
    return DocumentModel::Node::asSend();
  }

  //  Invoke *DocumentModel::Node::asInvoke()
  DocumentModel::Invoke *asInvoke() override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_StateCall7 call = reinterpret_cast<CuteDocumentModel_StateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Invoke *>(given);
    }
    return DocumentModel::Node::asInvoke();
  }

  //  Script *DocumentModel::Node::asScript()
  DocumentModel::Script *asScript() override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_StateCall8 call = reinterpret_cast<CuteDocumentModel_StateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Script *>(given);
    }
    return DocumentModel::Node::asScript();
  }

  //  Transition *DocumentModel::Node::asTransition()
  DocumentModel::Transition *asTransition() override {
    if (taken[9]) {
      int handled = 0;
      CuteDocumentModel_StateCall9 call = reinterpret_cast<CuteDocumentModel_StateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Transition *>(given);
    }
    return DocumentModel::Node::asTransition();
  }

  //  HistoryState *DocumentModel::Node::asHistoryState()
  DocumentModel::HistoryState *asHistoryState() override {
    if (taken[10]) {
      int handled = 0;
      CuteDocumentModel_StateCall10 call = reinterpret_cast<CuteDocumentModel_StateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::HistoryState *>(given);
    }
    return DocumentModel::Node::asHistoryState();
  }
};

//  DocumentModel::State::State(const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_ZN13DocumentModel5StateC1ERKNS_11XmlLocationE(
    const DocumentModel::XmlLocation *xmlLocation) {
  return new CuteDocumentModel_State(*xmlLocation);
}

//  void DocumentModel::State::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel5State3addEPNS_17StateOrTransitionE(
    DocumentModel::State *self,
    DocumentModel::StateOrTransition *s) {
  self->add(s);
}

//  State *DocumentModel::State::asState()
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_ZN13DocumentModel5State7asStateEv(
    DocumentModel::State *self) {
  return self->asState();
}

//  void DocumentModel::State::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel5State6acceptEPNS_11NodeVisitorE(
    DocumentModel::State *self,
    DocumentModel::NodeVisitor *visitor) {
  self->accept(visitor);
}

//  DocumentModel::State as the DocumentModel::StateOrTransition it is built
//      on
extern "C" Q_DECL_EXPORT
DocumentModel::StateOrTransition *ritual_cast_DocumentModel_State_DocumentModel_StateOrTransition(
    DocumentModel::State *self) {
  return static_cast<DocumentModel::StateOrTransition *>(self);
}

//  a Python function taken by a CuteDocumentModel_State, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_State(
    DocumentModel::State *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_State *>(self)->take(key, call);
}

//  void DocumentModel::State::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel5State3addEPNS_17StateOrTransitionE(
    DocumentModel::State *self,
    DocumentModel::StateOrTransition *s) {
  self->DocumentModel::State::add(s);
}

//  State *DocumentModel::State::asState()
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_own_ZN13DocumentModel5State7asStateEv(
    DocumentModel::State *self) {
  return self->DocumentModel::State::asState();
}

//  void DocumentModel::State::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel5State6acceptEPNS_11NodeVisitorE(
    DocumentModel::State *self,
    DocumentModel::NodeVisitor *visitor) {
  self->DocumentModel::State::accept(visitor);
}
