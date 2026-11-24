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
#include "qscxmlcompiler_p.h"
#include "qscxmlexecutablecontent_p.h"
#include <qxmlstream.h>
#include <qloggingcategory.h>
#include <qfile.h>
#include <qlist.h>
#include <qstring.h>
#ifndef BUILD_QSCXMLC
#include "qscxmlinvokableservice_p.h"
#include "qscxmldatamodel_p.h"
#include "qscxmlstatemachine_p.h"
#include "qscxmlstatemachine.h"
#include "qscxmltabledata_p.h"
#include <private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1144, as _ZN13DocumentModel4NodeD2Ev
inline DocumentModel::Node::~Node()
{
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1157, as _ZN13DocumentModel11DataElement6acceptEPNS_11NodeVisitorE
inline void DocumentModel::DataElement::accept(DocumentModel::NodeVisitor *visitor)
{
    visitor->visit(this);
}
//  -----------------------------------------------------------------------

//  A DocumentModel::DataElement that Python can take functions over in. Every DocumentModel::DataElement
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_DataElementCall0)(const void *, DocumentModel::NodeVisitor *, int *);
typedef void * (*CuteDocumentModel_DataElementCall1)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall2)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall3)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall4)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall5)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall6)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall7)(const void *, int *);
typedef void * (*CuteDocumentModel_DataElementCall8)(const void *, int *);
class CuteDocumentModel_DataElement : public DocumentModel::DataElement {
public:
  using DocumentModel::DataElement::DataElement;
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

  //  void DocumentModel::DataElement::accept(NodeVisitor *visitor)
  void accept(DocumentModel::NodeVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall0 call = reinterpret_cast<CuteDocumentModel_DataElementCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    DocumentModel::DataElement::accept(visitor);
  }

  //  If *DocumentModel::Node::asIf()
  DocumentModel::If *asIf() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall1 call = reinterpret_cast<CuteDocumentModel_DataElementCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::If *>(given);
    }
    return DocumentModel::Node::asIf();
  }

  //  Send *DocumentModel::Node::asSend()
  DocumentModel::Send *asSend() override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall2 call = reinterpret_cast<CuteDocumentModel_DataElementCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Send *>(given);
    }
    return DocumentModel::Node::asSend();
  }

  //  Invoke *DocumentModel::Node::asInvoke()
  DocumentModel::Invoke *asInvoke() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall3 call = reinterpret_cast<CuteDocumentModel_DataElementCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Invoke *>(given);
    }
    return DocumentModel::Node::asInvoke();
  }

  //  Script *DocumentModel::Node::asScript()
  DocumentModel::Script *asScript() override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall4 call = reinterpret_cast<CuteDocumentModel_DataElementCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Script *>(given);
    }
    return DocumentModel::Node::asScript();
  }

  //  State *DocumentModel::Node::asState()
  DocumentModel::State *asState() override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall5 call = reinterpret_cast<CuteDocumentModel_DataElementCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::Node::asState();
  }

  //  Transition *DocumentModel::Node::asTransition()
  DocumentModel::Transition *asTransition() override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall6 call = reinterpret_cast<CuteDocumentModel_DataElementCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Transition *>(given);
    }
    return DocumentModel::Node::asTransition();
  }

  //  HistoryState *DocumentModel::Node::asHistoryState()
  DocumentModel::HistoryState *asHistoryState() override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall7 call = reinterpret_cast<CuteDocumentModel_DataElementCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::HistoryState *>(given);
    }
    return DocumentModel::Node::asHistoryState();
  }

  //  Scxml *DocumentModel::Node::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_DataElementCall8 call = reinterpret_cast<CuteDocumentModel_DataElementCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::Node::asScxml();
  }
};

//  DocumentModel::DataElement::DataElement(const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::DataElement *ritual_ZN13DocumentModel11DataElementC1ERKNS_11XmlLocationE(
    const DocumentModel::XmlLocation *xmlLocation) {
  return new CuteDocumentModel_DataElement(*xmlLocation);
}

//  void DocumentModel::DataElement::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11DataElement6acceptEPNS_11NodeVisitorE(
    DocumentModel::DataElement *self,
    DocumentModel::NodeVisitor *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteDocumentModel_DataElement, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_DataElement(
    DocumentModel::DataElement *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_DataElement *>(self)->take(key, call);
}

//  void DocumentModel::DataElement::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel11DataElement6acceptEPNS_11NodeVisitorE(
    DocumentModel::DataElement *self,
    DocumentModel::NodeVisitor *visitor) {
  self->DocumentModel::DataElement::accept(visitor);
}
